from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


# outfit --< clothing_outfit >-- clothing_item

class Outfit(db.Model):
    __tablename__ = 'outfits'
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String())
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    # relationships has many clothing through ClothingOutfit
    user = relationship("User", back_populates='outfits')
    clothing = relationship(
        'ClothingItem',
        secondary='clothing_outfits',
        backref='outfits')


# join table  belongs to Outfit & ClothingItem

class ClothingOutfit(db.Model):
    __tablename__ = 'clothing_outfits'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    clothing_item_id = db.Column(db.Integer, ForeignKey('clothing_item.id'))
    outfit_id = db.Column(db.Integer, ForeignKey('outfit.id'))


class ClothingItem(db.Model):
    __tablename__ = 'clothing_items'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())

    # relationships has many outfits through ClothingOutfit
    outfits = relationship(
        'Outfit',
        secondary='clothing_outfits',
        back_populates='clothing_item')
# error message
# config.DevelopmentConfig
# INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
# INFO  [alembic.runtime.migration] Will assume transactional DDL.
# Traceback (most recent call last):
#   File "manage.py", line 14, in <module>
#     manager.run()
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/flask_script/__init__.py", line 417, in run
#     result = self.handle(argv[0], argv[1:])
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/flask_script/__init__.py", line 386, in handle
#     res = handle(*args, **config)
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/flask_script/commands.py", line 216, in __call__
#     return self.run(*args, **kwargs)
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/flask_migrate/__init__.py", line 95, in wrapped
#     f(*args, **kwargs)
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/flask_migrate/__init__.py", line 213, in migrate
#     command.revision(config, message, autogenerate=True, sql=sql,
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/command.py", line 214, in revision
#     script_directory.run_env()
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/script/base.py", line 489, in run_env
#     util.load_python_file(self.dir, "env.py")
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/util/pyfiles.py", line 98, in load_python_file
#     module = load_module_py(module_id, path)
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/util/compat.py", line 173, in load_module_py
#     spec.loader.exec_module(module)
#   File "<frozen importlib._bootstrap_external>", line 783, in exec_module
#   File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
#   File "migrations/env.py", line 96, in <module>
#     run_migrations_online()
#   File "migrations/env.py", line 90, in run_migrations_online
#     context.run_migrations()
#   File "<string>", line 8, in run_migrations
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/runtime/environment.py", line 846, in run_migrations
#     self.get_context().run_migrations(**kw)
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/runtime/migration.py", line 507, in run_migrations
#     for step in self._migrations_fn(heads, self):
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/command.py", line 190, in retrieve_migrations
#     revision_context.run_autogenerate(rev, context)
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/autogenerate/api.py", line 442, in run_autogenerate
#     self._run_environment(rev, migration_context, True)
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/autogenerate/api.py", line 481, in _run_environment
#     compare._populate_migration_script(
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/autogenerate/compare.py", line 25, in _populate_migration_script
#     _produce_net_changes(autogen_context, upgrade_ops)
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/autogenerate/compare.py", line 50, in _produce_net_changes
#     comparators.dispatch("schema", autogen_context.dialect.name)(
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/util/langhelpers.py", line 303, in go
#     fn(*arg, **kw)
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/autogenerate/compare.py", line 75, in _autogen_for_tables
#     [(table.schema, table.name) for table in autogen_context.sorted_tables]
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/util/langhelpers.py", line 230, in __get__
#     obj.__dict__[self.__name__] = result = self.fget(obj)
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/alembic/autogenerate/api.py", line 360, in sorted_tables
#     result.extend(m.sorted_tables)
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/sqlalchemy/sql/schema.py", line 4114, in sorted_tables
#     return ddl.sort_tables(
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/sqlalchemy/sql/ddl.py", line 1088, in sort_tables
#     for (t, fkcs) in sort_tables_and_constraints(
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/sqlalchemy/sql/ddl.py", line 1158, in sort_tables_and_constraints
#     dependent_on = fkc.referred_table
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/sqlalchemy/sql/schema.py", line 3240, in referred_table
#     return self.elements[0].column.table
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/sqlalchemy/util/langhelpers.py", line 855, in __get__
#     obj.__dict__[self.__name__] = result = self.fget(obj)
#   File "/home/will/.virtualenvs/my-style-python/lib/python3.8/site-packages/sqlalchemy/sql/schema.py", line 2042, in column
#     raise exc.NoReferencedTableError(
# sqlalchemy.exc.NoReferencedTableError: Foreign key associated with column 'clothing_outfits.clothing_item_id' could not find table 'clothing_item' with which to generate a foreign key to target column 'id'
