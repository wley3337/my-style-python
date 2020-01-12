from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Worn(db.Model):
    __tablename__ = 'worn'
    id = db.Column(db.Integer, primary_key=True)
    outfit_id = db.Column(db.Integer, ForeignKey('outfits.id'))
    date_worn = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime(), server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(), server_default=db.func.now(), server_onupdate=db.func.now())
    # relationships
    # belongs to
    outfit = relationship("Outfit", back_populates='worn')
