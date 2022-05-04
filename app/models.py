from sqlalchemy_utils import URLType
from app.extensions import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)

class Animal(db.Model):
  id = db.Column(db.Integer, primary_key=True)

class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)

class Island(db.Model):
  id = db.Column(db.Integer, primary_key=True)