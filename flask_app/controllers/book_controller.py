from flask import flash, redirect, render_template, request, session, url_for
from flask_bcrypt import Bcrypt

from flask_app import app
from flask_app.models.book_model import Book

# Routes
@app.route('/book/new')
def new_book():
  if 'user_id' not in session:
    return redirect('/')

  if session.get('admin') != 1:
    return redirect('/')

  return render_template ('new_book.html')

@app.route('/book/new/process', methods=['POST'])
def process_book_data():
  if not Book.validate(request.form):
    return redirect("/book/new")

  Book.create(request.form)
  return redirect('/admin_dashboard')

@app.route('/book/<int:id>/view')
def view_book(id):
  book = Book.get_by_id({'id': id})
  return render_template('view_book.html', book = book)

@app.route('/book/<int:id>/edit')
def edit_book(id):
  if 'user_id' not in session:
    return redirect('/')

  if session.get('admin') != 1:
    return redirect('/')

  book = Book.get_by_id({'id': id})

  if not book:
    return redirect('/')

  return render_template('edit_book.html', book = book)

@app.route('/book/<int:id>/update', methods=['POST'])
def update_book(id):
  if not Book.validate(request.form):
    return redirect(f"/book/{id}/edit")

  book_data = {**request.form, 'id': id}

  Book.update(book_data)
  return redirect('/admin_dashboard')
