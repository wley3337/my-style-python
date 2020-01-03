from server import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Outfit(db.Model):
    __tablename__ = 'outfits'
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.String())
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates='outfits')


User.outfits = relationship(
    'Outfits', order_by=Outfit.id, back_populates='user')
