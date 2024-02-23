# SearchSmartly

SearchSmartly is a Django project for importing and browsing Point of Interest (PoI) data from CSV, JSON, and XML files.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/SearchSmartly.git
   cd SearchSmartly

## Running 
1. Create a virtual environment (optional but recommended):
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run migrations to set up the database:
    ```
    python manage.py migrate
    ````
4. Create  super user
    ```
    python manage.py createsuperuser
    ```

## Usage
## Importing Data
    To import Point of Interest data from CSV, JSON, or XML files, use the provided management command importpoi. Pass the file paths as arguments to the command.

    python manage.py importpoi /path/to/file1.csv /path/to/file2.json /path/to/file3.xml

## Browsing Data
   1. You can browse the imported PoI data via the Django admin panel by running the following commands

    python manage.py runserver
    Navigate to http://127.0.0.1:8000/admin/ in your web browser.

    2. Log in using your superuser credentials.
    3. Click on the "Point of Interests" link to view and manage PoI data.

## Searching and Filtering
You can search for PoI data by internal ID or external ID using the search bar in the Django admin panel.
Use the category filter to filter PoI data by category.
