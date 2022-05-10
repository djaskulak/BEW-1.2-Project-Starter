from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, URL
from ac_app.models import AnimalPersonality

class AnimalForm(FlaskForm):
  """Form for adding/updating an Animal."""
  
  name = StringField('Name of Animal', validators=[DataRequired(), Length(min=3, max=80)])
  personality = SelectField('Personality Type of Animal', choices=AnimalPersonality.choices())
  photo_url = StringField('URL of Animal Photo')
  submit = SubmitField('Add this New Animal')

class ItemForm(FlaskForm):
  """Form for adding/updating an Item."""
  
  name = StringField('Name of Item', validators=[DataRequired(), Length(min=3, max=80)])
  price = IntegerField('Price of Product', validators=[DataRequired()])
  photo_url = StringField('URL of Item Photo')
  submit = SubmitField('Add this New Item')