# QuizyDonut!
## An online platform where you can create quiz to target your audience and if you want you can participate in other hosted events you can have fun!!

# Prequisites
## Technologies/Framework used
Here are the technologies/framework that we have been used.
* Django(Python)
* Bootstrap
* Javascript
* PostgreSQL
* Django Rest Framework

## Installation Process
* You should have virtualenvironment installed on your system for ubuntu user you can install it by typing ```pip install virtualenv``` on your terminal.
* Create a virtualenv for your project using ```virtualenv -p your/python3/path my_project```.
* Activate this virtualenv using ```source ~/.virtualenv/venvname/bin/activate``` from your root.
* All the libraries needed for this chapter are included in requirements.txt you can install them in your virtualenv by doing ```pip install -r requirements.txt```.

## Some useful things.
* You will need a secret key for running this application.
* Set up EMAIL_USER and EMAIL_USER_PASSWORD and set them up according to your gmail credentials for the password reset feature to work properly.
* Your database name and database password somewhere safe and not commit to your git.

## What you can do?

Make a .env file in your root directory and define all above variables in this file and import them in the main settings.py using the python os module by doing ```os.environ.get('VARIABLE_NAME)``` or ```os.getenv()``` and it will be imported to your project and you can work.
* At first install ```pip install dotenv``` this library will help you to import your variables from .env to your file.

