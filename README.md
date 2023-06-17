# HarnessAssessment

This is a Python-based web application which uses Django Rest Framework (DRF) to create APIs as per the requirement of harness assessment.

## Installation
To install the necessary dependencies, use the following command:

```shell
pip install -r requirements.txt
```
## Database Setup
To create the databases and required tables in the application, use the following commands:

```shell
python manage.py makemigrations
python manage.py migrate
```
## Running the Application
To run the application, use the following command:

```shell
python manage.py runserver
```
The application is also integrated with continuous integration (CI) to run the test cases.
