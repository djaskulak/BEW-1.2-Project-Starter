from flask import Blueprint, render_template, redirect, url_for, flash
from ac_app.models import Animal, Item
from ac_app.main.forms import AnimalForm, ItemForm
from flask_login import login_required
from ac_app.extensions import db

main = Blueprint('main', __name__)

##########################################
#           Routes                       #
##########################################

# HOME
@main.route('/')
def homepage():
  return render_template('home.html')

# NEW ANIMAL
@login_required
@main.route('/new_animal', methods=['GET', 'POST'])
def new_animal():
  form = AnimalForm()

  if form.validate_on_submit():
    new_animal = Animal(
      name = form.name.data,
      personality = form.personality.data,
      photo = form.photo.data
    )
    db.session.add(new_animal)
    db.session.commit()
    flash('A new animal has been added to your island.')
    return redirect(url_for('main.animal_detail', animal_id=new_animal.id))

  return render_template('new_animal.html', form=form)

# NEW ITEM
@login_required
@main.route('/new_item', methods=['GET', 'POST'])
def new_item():
  form = ItemForm()

  if form.validate_on_submit():
    new_item = Item(
      name = form.name.data,
      photo = form.photo.data,
      price = form.price.data
    )
    db.session.add(new_item)
    db.session.commit()
    flash('A new item has been added to your pockets.')
    return redirect(url_for('main.item_detail', item_id=new_item.id))

  return render_template('new_item.html', form=form)

# ANIMAL DETAIL
@login_required
@main.route('/animal/<animal_id>', methods=['GET', 'POST'])
def animal_detail(animal_id):
  animal = Animal.query.get(animal_id)
  form = AnimalForm(obj=animal)

  if form.validate_on_submit():
    animal.name = form.name.data
    animal.personality = form.personality.data
    animal.photo = form.photo.data
    print("************")
    print(animal)
    print(animal.name)
    print(animal.personality)

    db.session.add(animal)
    db.session.commit()
    flash('The animal has been updated successfully.')
    return redirect(url_for('main.animal_detail', animal_id=animal.id))

  animal = Animal.query.filter_by(id=animal_id).one()
  return render_template('animal_detail.html', animal=animal, form=form)

# ITEM DETAIL
@login_required
@main.route('/item/<item_id>', methods=['GET', 'POST'])
def item_detail(item_id):
  item = Item.query.get(item_id)
  form = ItemForm(obj=item)

  if form.validate_on_submit():
    item.name = form.name.data
    item.price = form.price.data
    item.photo = form.photo.data
    print("************")
    print(item)
    print(item.name)
    print(item.price)

    db.session.add(item)
    db.session.commit()
    flash('The item has been updated successfully.')
    return redirect(url_for('main.item_detail', item_id=item.id))

  item = Item.query.filter_by(id=item_id).one()
  return render_template('item_detail.html', item=item, form=form)