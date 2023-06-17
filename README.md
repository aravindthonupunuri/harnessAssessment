harnessAssessment

This is a Python based web application which uses DRF to create APIs as per the requirement of harness assessment.

To install necessary dependencies 
use the following command
pip install requirements.txt

To create the databases and required tables in the application
use the following commands
python manage.py makemigrations
python manage.py makemigrate

To run the application 
use the following command
python manage.py runserver

To test the application 
use the following command
python manage.py test api.tests
The application is also integrated with CI to run the test cases.
