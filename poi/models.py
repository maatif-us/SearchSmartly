from django.db import models


class PointOfInterest(models.Model):
    internal_id = models.AutoField(primary_key=True)
    external_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(max_length=255)
    avg_ratings = models.FloatField()
    description = models.TextField(blank=True, null=True)

    def __self__(self):
        return self.name

    def __str__(self):
        return f"{self.name}"
