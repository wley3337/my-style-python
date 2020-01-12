from app import db
from sqlalchemy import ForeignKey


class ClothingCategory(db.Model):
    __tablename__ = 'clothing_categories'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, ForeignKey('category.id'))
    clothing_item_id = db.Column(db.Integer, ForeignKey('clothing_items.id'))
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(), server_default=db.func.now(), server_onupdate=db.func.now())
