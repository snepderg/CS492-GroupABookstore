from flask_app import app
from flask import render_template, session, redirect, request, flash, url_for
from flask_bcrypt import Bcrypt
from flask_app.models.user_model import User
from flask_app.models.book_model import Book
import re

bcrypt = Bcrypt(app)

# Home route with login and registration, if user logged in, redirects to dash
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

# Process any registration attempts and redirects to dashboard on success
@app.route('/users/register', methods=['POST'])
def process_registration():
    if not User.validate(request.form):
      return redirect('/')
    pass_hash = bcrypt.generate_password_hash(request.form['password'])
    if re.search(r'@dundermifflin\.com$', request.form['email']):
      admin = 1
    else:
      admin = 0
    data = {
      **request.form,
      'admin': admin,
      'password': pass_hash,
      'confirm_password': pass_hash
      }
    user_id = User.create(data)
    session['user_id'] = user_id
    session['admin'] = admin
    if admin == 1:
      return redirect(url_for('admin_dashboard'))
    else:
      return redirect(url_for('dashboard'))

@app.route('/users/login', methods=['POST'])
def process_login():
    potential_user = User.get_by_email(request.form)
    if not potential_user:
        flash('Invalid credentials. Try again.', 'log')
        return redirect('/')
    elif not bcrypt.check_password_hash(potential_user.password, request.form['password']):
        flash('Invalid credentials. Try again.', 'log')
        return redirect('/')
    session['user_id'] = potential_user.id
    session['admin'] = potential_user.admin
    if session.get('admin') != 1:
      return redirect('/dashboard')
    else:
      return redirect(url_for('admin_dashboard'))

@app.route('/users/logout')
def logout():
    del session['user_id']
    return redirect('/')

@app.route('/dashboard')
def dashboard():
  if 'user_id' not in session:
    return redirect('/')
  one_user = User.get_by_id({'id':session['user_id']})
  books = Book.get_all()
  return render_template('dashboard.html', one_user = one_user, books = books)

@app.route('/admin_dashboard')
def admin_dashboard():
  if session.get('admin') != 1:
    return redirect('/dashboard')
  one_user = User.get_by_id({'id':session['user_id']})
  books = Book.get_all()
  return render_template('admin_dashboard.html', one_user = one_user, books = books)
