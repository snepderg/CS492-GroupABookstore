import re

from flask import flash, redirect, render_template, request, session, url_for
from flask_bcrypt import Bcrypt

from flask_app import app
from flask_app.models.book_model import Book
from flask_app.models.order_model import Order
from flask_app.models.user_model import User

bcrypt = Bcrypt(app)

# Landing Page route for first visitors, if user logged in, redirects to dash
@app.route('/')
@app.route('/#<id>')
def landing():
    if 'user_id' in session:
        return redirect('/dashboard')

    authors_books = {
      author: [book for book in Book.get_by_author({'author': author})]
      for author in ['Terry Pratchett', 'J. D. Salinger', 'Stephen King']
    }

    genres_books = {
      genre: [book for book in Book.get_by_genre({'genre': genre})]
      for genre in ['Fantasy', 'Historical Fiction', 'Horror']
    }

    return render_template('index.html', authors_books = authors_books, genres_books = genres_books)

# Route for login and registration page, if user logged in, redirects to dash
@app.route('/login_registration')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('login_registration.html')

# Process any registration attempts and redirects to dashboard on success
@app.route('/users/register', methods=['POST'])
def process_registration():
    if not User.validate(request.form):
      return redirect('/login_registration')
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
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
  if 'user_id' not in session:
    return redirect('/')
  if session.get('admin') == 1:
    return redirect('/admin_dashboard')
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
