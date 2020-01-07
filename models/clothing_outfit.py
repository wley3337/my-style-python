from app import db
from sqlalchemy import ForeignKey


class ClothingOutfit(db.Model):
    __tablename__ = 'clothing_outfits'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    clothing_item_id = db.Column(db.Integer, ForeignKey('clothing_item.id'))
    outfit_id = db.Column(db.Integer, ForeignKey('outfit.id'))
