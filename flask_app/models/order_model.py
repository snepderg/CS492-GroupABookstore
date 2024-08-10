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

  @classmethod
  def create_order(cls, data):
    query = """
      INSERT INTO orders (total, customer_id)
      VALUES (%(total)s, %(customer_id)s)
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
  def get_one_with_books(cls, data):
    query = """
        SELECT * FROM orders JOIN 
        books_in_orders ON orders.id = books_in_orders.order_id 
        JOIN books ON books_in_orders.book_id = books.id
        WHERE orders.id = %(id)s
    """
    results = connectToMySQL(cls.db).query_db(query, data)
    order = cls(results[0])
    for row in results: 
      book_data = {
        'id' : row['id'],
        'title' : row['title'],
        'genre' : row['genre'],
        'price' : row['price'],
        'author' : row['author']
      }
      book = book_model.Book(book_data)
      order.books.append(book)
    return order