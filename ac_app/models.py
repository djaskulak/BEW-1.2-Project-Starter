from sqlalchemy_utils import URLType
from app.extensions import db

class AnimalPersonality(FormEnum):
  JOCK = 'Jock'
  CRANKY = 'Cranky'
  PEPPY = 'Peppy'
  SISTERLY = 'Sisterly'
  LAZY = 'Lazy'
  NORMAL = 'Normal'
  SNOOTY = 'Snooty'

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name 
  island 
  animals 
  items 

class Animal(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id 
  personality 
  name 
  island 
  items 
  photo 

class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  owner_id 
  name 
  photo 

class Island(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id 
  name 
  animals 