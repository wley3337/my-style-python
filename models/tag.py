from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(), server_default=db.func.now(), server_onupdate=db.func.now())
    # relationships
    # has many through
    clothing = relationship(
        'ClothingItem',
        secondary='clothing_tags',
        back_populates='tags'
    )
