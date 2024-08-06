from flask_app import app
from flask import render_template, session, redirect, request, flash, url_for
from flask_bcrypt import Bcrypt
from flask_app.models.book_model import Book

@app.route('/book/new')
def new_book():
  if 'user_id' not in session:
    return redirect('/')
  return render_template ('new_book.html')

@app.route('/book/new/process', methods=['POST'])
def process_book_data():
  Book.create(request.form)
  return redirect('/dashboard')

# setup route for /book/<int:id>/edit
@app.route('/book/<int:id>/edit')
def edit_book(id):
  if 'user_id' not in session:
    return redirect('/')

  book = Book.get_by_id({'id': id})

  if not book:
    return redirect('/')

  return render_template('edit_book.html', book = book)