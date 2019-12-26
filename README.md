# Python with PostgreSQL backend 


# Install:

* create a PostgreSQL database name: `my-style`

* `pip install -r requirements.txt`
* create a `./.env` file containing:
 
    export APP_SETTINGS="config.DevelopmentConfig"
  
http://127.0.0.1:35825/?key=ba86d9a2-e60f-44f0-8be8-673161fe7105

# Notes:

* lock in new dependancies: `pip freeze > requirements.txt`
* Start local env: `source env/bin/activate`
* End local env: `deactivate`
* [Local ENV info](https://realpython.com/python-virtual-environments-a-primer/)

* [tutorial for ref](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)


### Migrations 
  * Create the database in terminal under postgres user: `suod -iu postgres` under manjaro linux
  * `python manage.py db initi` sets up the Alembic first time `manage.py` is the setup file location
  * `python manage.py db migrate` pulls migrations from all model deffinitions 
  * `python manage.py db upgrade` updates the database from all migrations