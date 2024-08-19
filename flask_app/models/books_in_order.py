from flask_app.config.mysqlconnection import connectToMySQL


class Books_in_Order:
  db = 'page_turners'
  def __init__(self,data):
    self.id = data['id']
    self.book_id = data['book_id']
    self.order_id = data['order_id']


  @classmethod
  def all_books_for_order(cls, data):
    query = """
      SELECT * FROM  books_in_orders WHERE order_id = %(order_id)s
    """
    results = connectToMySQL(cls.db).query_db(query, data)
    books = []
    for book in results:
      books.append(cls(book))
    return books
  
  @classmethod
  def delete_one_book(cls, data):
    query = """
      DELETE FROM books_in_orders WHERE id = %(id)s;
    """
    return connectToMySQL(cls.db).query_db(query, data)
  
  @classmethod
  def find_one_entry(cls, data):
    query = """
      SELECT * FROM books_in_orders WHERE id = %(id)s;
    """
    result = connectToMySQL(cls.db).query_db(query, data)
    if len(result) < 1:
      return False
    return cls(result[0])