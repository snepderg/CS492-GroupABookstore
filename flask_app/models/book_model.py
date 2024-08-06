from flask_app.config.mysqlconnection import connectToMySQL

class Book:
  db = 'page_turners'
  def __init__(self, data):
    self.id = data['id']
    self.title = data['title']
    self.genre = data['genre']
    self.author = data['author']
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
  def get_all(cls):
    query = """
          SELECT * FROM books;
      """
    results = connectToMySQL(cls.db).query_db(query)
    books = []
    for book in results:
      books.append(cls(book))
    return books