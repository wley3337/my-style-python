from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    # associate the table name with the results
    __tablename__ = 'results'
    # this is the schema defined in the example
    # id for record
    # this is integer type and primary_key
    id = db.Column(db.Integer, primary_key=True)
    # url that the page that we did a 'word count from'
    # string type
    url = db.Column(db.String())
    # makes sure all the results are in JSON format
    # all the words counted  <-- this is example specific
    # this is actually type json which is not supported by default in alchemy so it needed to be explicitly imported and stated
    result_all = db.Column(JSON)
    # all the words counted minus the 'stop words' <-- this is example specific
    result_no_stop_words = db.Column(JSON)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(), server_default=db.func.now(), server_onupdate=db.func.now())

    # not needed with the ORM the init will be under the column names from table defs
    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)


# class ChildModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

#     model_id = db.Column(db.Integer, ForeignKey('table_name.column_name'))

#     modelProperty = relationship(
#         'ClassName of Relationship',
#         secondary='join_table_name',
#         back_populates='correspondingForeignModelProperty')
