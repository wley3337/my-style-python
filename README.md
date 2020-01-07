# Python with PostgreSQL backend 


# Install:

* create a PostgreSQL database name: `my-style`

* `pip install -r requirements.txt`
* create a `./.env` file containing:
 
    export APP_SETTINGS="config.DevelopmentConfig"


# Notes:

* lock in new dependancies: `pip freeze > requirements.txt`
* Start local env: `source env/bin/activate`
* End local env: `deactivate`
* [Local ENV info](https://realpython.com/python-virtual-environments-a-primer/)

* [tutorial for ref](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)
* quick [SQLAlchemy ref](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#relationship-patterns)
* start the db `sudo systemctl start postgresql.service`
* stop the db `sudo systemctl stop postgresql.service`


### Migrations 
  * Create the database in terminal under postgres user: `suod -iu postgres` under manjaro linux
  From primiary user: 
  * `python manage.py db initi` sets up the Alembic first time `manage.py` is the setup file location
  * `python manage.py db migrate` pulls migrations from all model deffinitions 
  * `python manage.py db upgrade` updates the database from all migrations
  