## Food Management System - National Institute of Technology, Andhra Pradesh

Hosted at: http://hmsepc.herokuapp.com/

### Dev Environment Setup - Windows: 

**Requires python and pip**

#### Setup Django and python packages(CMD/Terminal at PreferredDirectory)
 - `git clone https://github.com/EswarSaiBandi/web_Project/`
 - `python -m venv myvenv`
 - `myvenv/Scripts/activate`
 - `pip install -r requirements.txt`
 - Create .env file inside Django/hmsdb with:
```
SECRET_KEY=&54=+66-wt)d319m09du8+((^lb+-(m4r1bi&&^fgv7@u6+6h6
DEBUG=True
ENVIRONMENT=development
APP_EMAIL=<placeholder_email>
APP_EMAIL_PASSWORD=<placeholder_email_password>
```
Key generated at https://miniwebtool.com/django-secret-key-generator/

#### Setup MySQL DB(In MySQL CLI or Workbench)
 - `CREATE SCHEMA fmsdb;`
 - `CREATE USER 'fmsadmin' IDENTIFIED WITH mysql_native_password BY '12345';`
 - `grant all privileges on fmsdb.* to 'fmsadmin';`
 - Please follow instructions given at https://medium.com/@omaraamir19966/connect-django-with-mysql-database-f946d0f6f9e3 to install **mysqlclient** inside PreferredDirectory/Django

#### Migrate, Create Superuser and Run Server(CMD/Terminal at PreferredDirectory/HMS_Django)
 - `python manage.py migrate`
 - `python manage.py createsuperuser`
 - Fill in required details
 - `python manage.py runserver`
 - Visit **http://localhost:8000/admin** and login using the previously entered credentials.
 - Create Officials, Students and Blocks.
 - Visit **http://localhost:8000/** in another browser window and Sign Up with any of the previously entered emails of Officials or Students.
 - On sign up verification link will be sent through mail in production, in development visit the CMD/Terminal where you ran `python manage.py runserver` to find the verification link and open it in the browser.
 - Login using the credentials previously used to sign up.

