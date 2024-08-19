from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book_model


class Order:
  db = 'page_turners'
  def __init__(self, data):
    self.id = data['id']
    self.total = data['total']
    # self.book_id = data['book_id']
    self.customer_id = data['customer_id']
    self.books = []
    self.each_book = []

  @classmethod
  def create_order(cls, data):
    query = """
      INSERT INTO orders (total, customer_id, order_number)
      VALUES (%(total)s, %(customer_id)s, %(order_number)s)
    """
    return connectToMySQL(cls.db).query_db(query, data)
  
  @classmethod
  def add_book_to_order(cls, data):
    query = """
      INSERT INTO books_in_orders (book_id, order_id)
      VALUES (%(book_id)s, %(order_id)s)
    """
    return connectToMySQL(cls.db).query_db(query, data)
  
  @classmethod
  def get_by_id(cls, data):
    query = """
        SELECT * FROM orders WHERE id = %(id)s;
      """
    result = connectToMySQL(cls.db).query_db(query, data)
    if len(result) < 1:
      return False
    return cls(result[0])
  
  @classmethod
  def get_order_by_customer(cls, data):
    query = """
      SELECT * FROM orders WHERE customer_id = %(customer_id)s;
    """
    result = connectToMySQL(cls.db).query_db(query, data)
    return cls(result[0])
  
  @classmethod
  def get_one_with_books(cls, data):
    query = """
        SELECT * FROM orders JOIN 
        books_in_orders ON orders.id = books_in_orders.order_id 
        JOIN books ON books_in_orders.book_id = books.id
        WHERE orders.id = %(id)s
    """
    results = connectToMySQL(cls.db).query_db(query, data)
    if len(results) < 1:
      return False
    order = cls(results[0])
    for row in results: 
      book_data = {
        'id' : row['books.id'],
        'title' : row['title'],
        'genre' : row['genre'],
        'price' : row['price'],
        'author' : row['author'],
        'quantity_in_stock' : row['quantity_in_stock'],
        'user_id' : row['user_id'],
        'created_at' : row['books.created_at'],
        'updated_at' : row['books.updated_at'],
        'book_in_order_id' : row['books_in_orders.id']
      }
      book = book_model.Book(book_data)
      print(book_data)
      order.books.append(book)
    return order
  
  @classmethod
  def update_order(cls, data):
    query = """
      UPDATE orders SET total = %(total)s WHERE id = %(id)s;
      """
    return connectToMySQL(cls.db).query_db(query, data)
  
  @classmethod
  def delete_book(cls, data):
    query = """
      DELETE FROM books_in_orders WHERE book_id = %(book_id)s AND order_id = %(order_id)s;
    """
    return connectToMySQL(cls.db).query_db(query, data)
  
  @classmethod
  def delete_order(cls, data):
    query = """
      DELETE FROM orders WHERE id = %(id)s;
    """
    return connectToMySQL(cls.db).query_db(query, data)
