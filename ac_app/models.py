from sqlalchemy_utils import URLType
from ac_app.extensions import db

class AnimalPersonality(FormEnum):
  JOCK = 'Jock'
  CRANKY = 'Cranky'
  PEPPY = 'Peppy'
  SISTERLY = 'Sisterly'
  LAZY = 'Lazy'
  NORMAL = 'Normal'
  SNOOTY = 'Snooty'
  OTHER = 'Other'

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  island = db.Column(db.Integer, db.ForeignKey('island.id'), nullable=False)
  animals = db.relationship('Animal', back_populates='animals')
  items = db.relationship('Animal', back_populates='user')

class Animal(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  personality = db.Column(db.Enum(AnimalPersonality), default=AnimalPersonality.OTHER)
  name = db.Column(db.String(80), nullable=False)
  island = db.Column(db.Integer, db.ForeignKey('island.id'), nullable=False)
  items = db.relationship('Animal', back_populates='island')
  photo = db.Column(URLType)

class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  name = db.Column(db.String(80), nullable=False)
  photo = db.Column(URLType)

class Island(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  name = db.Column(db.String(80), nullable=False)
  animals = db.relationship('Animal', back_populates='island')