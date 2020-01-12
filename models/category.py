from app import db
from sqlalchemy.orm import relationship


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    # relationships
    # many to many
    clothing_items = relationship(
        "ClothingItem",
        secondary='clothing_category',
        back_populates='category')
