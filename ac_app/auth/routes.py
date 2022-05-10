from flask import Blueprint, request, render_template, redirect, url_for, flash
from ac_app.models import User
from ac_app.auth.forms import SignUpForm, LoginForm
from ac_app import bcrypt
from flask_login import login_user, logout_user, login_required
import flask_login
from flask import Blueprint
from ac_app.extensions import db

main = Blueprint('main', __name__)

##########################################
#              Auth Routes               #
##########################################

@main.route('/signup', methods=['GET', 'POST'])
def signup():
  print('in signup')
  form = SignUpForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(
      username=form.username.data,
      password=hashed_password
    )
    db.session.add(user)
    db.session.commit()
    flash('Account Created.')
    print('created')
    return redirect(url_for('main.login'))
  print(form.errors)
  return render_template('signup.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, remember=True)
        next_page = request.args.get('next')
        return redirect(next_page if next_page else url_for('main.homepage'))
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.homepage'))