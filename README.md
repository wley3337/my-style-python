# Python with PostgreSQL backend

# Install:

- create a PostgreSQL database name: `my-style`

- `pip install -r requirements.txt`
  - if you're getting an error on Mac OS X for Psycopy2 install the binary using: `pip install psycopg2-binary`
- create a `./.env` file containing:

  export APP_SETTINGS="config.DevelopmentConfig"

# Notes:

- Model def:

  - model_id = db.Column(db.Integer, ForeignKey('table_name.column_name'))

  - modelProperty = relationship(
    'ClassName of ForeignModel',
    secondary='join_table_name',
    back_populates='correspondingForeignModelProperty')
  - [time stamp](https://dev.mysql.com/doc/refman/5.6/en/server-system-variables.html#sysvar_explicit_defaults_for_timestamp) to look at

- lock in new dependencies: `pip freeze > requirements.txt`
- Start local env: `source env/bin/activate`
- End local env: `deactivate`
- [Local ENV info](https://realpython.com/python-virtual-environments-a-primer/)

- [tutorial for ref](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)
- quick [SQLAlchemy ref](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#relationship-patterns)
- start the db `sudo systemctl start postgresql.service`
- stop the db `sudo systemctl stop postgresql.service`

### Migrations

- Create the database in terminal under postgres user: `sudo -iu postgres` under manjaro linux
  From primiary user:
- `python manage.py db initi` sets up the Alembic first time `manage.py` is the setup file location
- `python manage.py db migrate` pulls migrations from all model deffinitions
- `python manage.py db upgrade` updates the database from all migrations
