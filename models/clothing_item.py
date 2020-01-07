from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class ClothingItem(db.Model):
    __tablename__ = 'clothing_items'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    outfit = relationship("Outfit", back_populates='clothing_items')
    # relationships
    outfits = relationship(
        'Outfit',
        secondary='clothing_outfits',
        back_populates='clothing_item')
