from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Closet(db.Model):
    __tablename__ = 'closets'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    updated_at = db.Column(db.DateTime())

    # relationships
    # belongs to
    user = relationship("User", back_populates='closets')
    # has many
    clothing = relationship("ClothingItem")
