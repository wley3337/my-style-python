# from datetime import datetime
from app import db
# from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class ClothingItem(db.Model):
    __tablename__ = 'clothing_items'
    id = db.Column(db.Integer, primary_key=True)
    closet_id = db.Column(db.Integer, ForeignKey('closet.id'))
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(), server_default=db.func.now(), server_onupdate=db.func.now())
    # relationships
    # belongs to
    closet = relationship("Closet", back_populates='clothing')
    # many to many through
    outfits = relationship(
        'Outfit',
        secondary='clothing_outfits',
        back_populates='clothing')
