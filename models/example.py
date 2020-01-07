from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


# outfit --< clothing_outfit >-- clothing_item

class Outfit(db.Model):
    __tablename__ = 'outfits'
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String())
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    # relationships has many clothing through ClothingOutfit
    user = relationship("User", back_populates='outfits')
    clothing = relationship(
        'ClothingItem',
        secondary='clothing_outfits',
        back_populates='outfits')


# join table  belongs to Outfit & ClothingItem

class ClothingOutfit(db.Model):
    __tablename__ = 'clothing_outfits'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    clothing_item_id = db.Column(db.Integer, ForeignKey('clothing_item.id'))
    outfit_id = db.Column(db.Integer, ForeignKey('outfit.id'))


class ClothingItem(db.Model):
    __tablename__ = 'clothing_items'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    outfit = relationship("Outfit", back_populates='clothing_items')

    # relationships has many outfits through ClothingOutfit
    outfits = relationship(
        'Outfit',
        secondary='clothing_outfits',
        back_populates='clothing_item')
