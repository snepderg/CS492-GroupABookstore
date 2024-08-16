from flask import flash, session

from flask_app.config.mysqlconnection import connectToMySQL


class Book:
  db = 'page_turners'
  def __init__(self, data):
    self.id = data['id']
    self.title = data['title']
    self.genre = data['genre']
    self.author = data['author']
    self.price = data['price']
    self.quantity_in_stock = data['quantity_in_stock']
    self.user_id = data['user_id']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def create(cls, data):
    query = """
        INSERT INTO books (title, genre, author, price, quantity_in_stock, user_id)
        VALUES (%(title)s, %(genre)s, %(author)s, %(price)s, %(quantity_in_stock)s, %(user_id)s);
    """
    return connectToMySQL(cls.db).query_db(query, data)

  @classmethod
  def update(cls, data):
    query = """
        UPDATE books SET title = %(title)s, genre = %(genre)s, author = %(author)s, price = %(price)s, quantity_in_stock = %(quantity_in_stock)s, user_id = %(user_id)s
        WHERE id = %(id)s;
    """
    return connectToMySQL(cls.db).query_db(query, data)
  
  @classmethod
  def update_book_quantity(cls, data):
    query = """
      UPDATE books SET quantity_in_stock = %(quantity_in_stock)s WHERE id = %(id)s;
    """
    return connectToMySQL(cls.db).query_db(query, data)

  @classmethod
  def delete(cls, data):
    query = """
        DELETE FROM books WHERE id = %(id)s;
    """
    return connectToMySQL(cls.db).query_db(query, data)

  @classmethod
  def get_all(cls):
    query = """
        SELECT * FROM books;
      """
    results = connectToMySQL(cls.db).query_db(query)
    books = []
    for book in results:
      books.append(cls(book))
    return books

  @classmethod
  def get_by_id(cls, data):
    query = """
        SELECT * FROM books WHERE id = %(id)s;
      """
    result = connectToMySQL(cls.db).query_db(query, data)
    if len(result) < 1:
      return False
    return cls(result[0])

  @staticmethod
  def validate(data):
    is_valid = True

    # Unique Title validation
    all_books = Book.get_all()
    if len(data['title']) < 1:
      is_valid = False
      flash('Title is required.')
    elif len(data['title']) < 2:
      is_valid = False
      flash('Title must be at least 2 characters.')
    else:
      for one_book in all_books:
        if one_book.title.lower() == data['title'].lower():
          is_valid = False
          flash('Title already exists.')

    # Genre validation with keeping invalid admin input
    if len(data['genre']) < 1:
        is_valid = False
        session['genre'] = data['genre']
        flash('Genre is required.')
    elif len(data['genre']) < 3:
        is_valid = False
        session['genre'] = data['genre']
        flash('Genre must be at least 3 characters.')

    # Price validation
    if len(data['price']) < 1:
        is_valid = False
        flash('Price is required.')
    elif float(data['price']) < 1:
        is_valid = False
        flash('Price must be greater than 0.')

    # Quantity validation
    if len(data['quantity_in_stock']) < 1:
        is_valid = False
        flash('Quantity in stock is required.')
    elif int(data['quantity_in_stock']) < 1:
        is_valid = False
        flash('Quantity must be greater than 0.')

    return is_valid
  
  @staticmethod
  def validate_edit(data):
    is_valid = True

    # Unique Title validation
    all_creations = Book.get_all()
    this_creation = Book.get_by_id(data)
    if len(data['title']) < 1:
      is_valid = False
      flash('Title is required.')
    elif len(data['title']) < 2:
      is_valid = False
      flash('Title must be at least 2 characters.')
    else:
      for one_creation in all_creations:
        if one_creation.title.lower() == data['title'].lower() and this_creation.title.lower() != one_creation.title.lower():
          is_valid = False
          flash('Title already exists.')
    
    # Description validation with keeping invalid user input
    if len(data['genre']) < 1:
        is_valid = False
        session['genre'] = data['genre']
        flash('Genre is required.')
    elif len(data['genre']) < 3:
        is_valid = False
        session['genre'] = data['genre']
        flash('Genre must be at least 3 characters.')

    # Price validation
    if len(data['price']) < 1:
        is_valid = False
        flash('Price is required.')
    elif float(data['price']) < 1:
        is_valid = False
        flash('Price must be greater than 0.')

    # Quantity validation
    if len(data['quantity_in_stock']) < 1:
        is_valid = False
        flash('Quantity is required.')
    elif int(data['quantity_in_stock']) < 1:
        is_valid = False
        flash('Quantity must be greater than 0.')

    return is_valid