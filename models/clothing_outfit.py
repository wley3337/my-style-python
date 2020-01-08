from app import db
from sqlalchemy import ForeignKey
# from datetime import datetime


class ClothingOutfit(db.Model):
    __tablename__ = 'clothing_outfits'
    id = db.Column(db.Integer, primary_key=True)
    # created_at = db.Column(db.DateTime())
    # updated_at = db.Column(db.DateTime(), default=datetime.utcnow)
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(), server_default=db.func.now(), server_onupdate=db.func.now())
    clothing_item_id = db.Column(db.Integer, ForeignKey('clothing_items.id'))
    outfit_id = db.Column(db.Integer, ForeignKey('outfits.id'))
