import csv
import json

from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from poi.models import PointOfInterest


class Command(BaseCommand):
    help = "Import Point of Interest (PoI) files"  # Help message for the management command

    def add_arguments(self, parser):
        parser.add_argument(
            "files",
            nargs="+",
            type=str,
            help="List of file paths to import",  # Description of the argument
        )

    def handle(self, *args, **options):
        """
        Entry point for the management command. Determines the file type and calls the appropriate import method.
        """
        for file_path in options["files"]:
            file_extension = file_path.split(".")[-1]  # Extracting file extension
            if file_extension.lower() == "csv":
                self.import_csv(file_path)
            elif file_extension.lower() == "json":
                self.import_json(file_path)
            elif file_extension.lower() == "xml":
                self.import_xml(file_path)
            else:
                self.stdout.write(
                    self.style.ERROR(
                        f"Unsupported file format: {file_extension}"
                    )  # Error message for unsupported file format
                )

    def import_csv(self, file_path):
        """
        Import data from a CSV file.
        """
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)

            count = 1
            for row in reader:
                poi = PointOfInterest(  # Creating PointOfInterest object
                    external_id=row["poi_id"],
                    name=row["poi_name"],
                    latitude=row["poi_latitude"],
                    longitude=row["poi_longitude"],
                    category=row["poi_category"],
                    avg_ratings=self._calculate_average_ratings(
                        list(
                            map(float, row["poi_ratings"][1:-1].split(","))
                        )  # Convert each rating string to a floating-point number using map(),
                    ),
                )

                poi.save()

    def import_json(self, file_path):
        """
        Import data from a JSON file.
        """
        with open(file_path, "r") as file:
            data = json.load(file)

            for item in data:
                poi = PointOfInterest(  # Creating PointOfInterest object
                    external_id=item["id"],
                    name=item["name"],
                    description=item["description"],
                    latitude=item["coordinates"]["latitude"],
                    longitude=item["coordinates"]["longitude"],
                    category=item["category"],
                    avg_ratings=self._calculate_average_ratings(item["ratings"]),
                )

                poi.save()

    def import_xml(self, file_path):
        """
        Import data from an XML file.
        """
        with open(file_path, "r") as file:
            # Parse the XML file using BeautifulSoup
            soup = BeautifulSoup(file, "xml")

        # extracting data records
        data_records = soup.find_all("DATA_RECORD")

        for poi_elem in data_records:
            poi = PointOfInterest(  # Creating PointOfInterest object
                external_id=poi_elem.find("pid").text,
                name=poi_elem.find("pname").text,
                category=poi_elem.find("pcategory").text,
                latitude=poi_elem.find("platitude").text,
                longitude=poi_elem.find("plongitude").text,
                avg_ratings=self._calculate_average_ratings(
                    list(map(int, poi_elem.find("pratings").text.split(",")))
                ),
            )
            poi.save()

    def _calculate_average_ratings(self, avg_ratings):
        return sum(avg_ratings) / len(avg_ratings)
