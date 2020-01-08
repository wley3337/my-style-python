from app import db
from sqlalchemy.orm import relationship
"""
    User Model: first_name, last_name, username
    Has Many: outfits, closets
"""


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    username = db.Column(db.String())

    # relationships
    outfits = relationship('Outfit', back_populates='user')
    closets = relationship('Closet', back_populates='user')

    # this is how python will return objects (at least in terminal, not sure about db queries)
    def __repr__(self):
        return'<id {}, username {}, outfits {}>'.format(self.id, self.username, self.outfits)
