My rihal_FSWD Django Project
This project is a Django web application that allows the user to create and modify tables using CRUD OPERATIONS

Installation
To install this project, follow these steps:

Clone the repository to your local machine
Install the required dependencies using pip install -r requirements.txt
Create a new virtual environment using python -m venv env
Activate the virtual environment using source env/bin/activate
Run database migrations using python manage.py migrate

Usag
To start the development server, run python manage.py runserver. This will start the server on http://localhost:8000/.

To create a new student, navigate to http://localhost:8000/student/ and fill out the registration form.

To edit or delete a student, navigate to http://localhost:8000/student/list/.

To view a list of all the records, navigate to http://localhost:8000/student/list/.

To view statistics such as the count of students per class, count of students per country,
and average age of students, navigate to http://localhost:8000/student/statistics/.



Configurations
Database
This project uses PostgreSQL as its database backend. To configure the database connection,
you will need to set the following environment variables in a .env file in the root of your project:
DATABASE_URL=postgres://postgres:8aLJab@localhost:5432/rihalDB

Secret Key
To generate a new secret key for your Django application, run the following command in your terminal:
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
Copy the output of this command and set it as the value of the SECRET_KEY environment variable in your .env file:
SECRET_KEY=your_secret_key_value


License
This project is released under the MIT License.
