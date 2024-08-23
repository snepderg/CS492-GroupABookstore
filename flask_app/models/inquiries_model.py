from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model


class Inquiry:
  db = 'page_turners'
  def __init__(self,data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.category = data['category']
    self.description = data['description']
    self.order_number = data['order_number']
    self.user_id = data['user_id']
    self.reporter = None
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def create_inquiry(cls, data):
    query = """
      INSERT INTO inquiries (first_name, last_name, category, description, order_number, user_id)
      VALUES (%(first_name)s, %(last_name)s, %(category)s, %(description)s, %(order_number)s, %(user_id)s);
    """
    return connectToMySQL(cls.db).query_db(query, data)
  
  @classmethod
  def view_all_inquiries(cls):
    query = """
      SELECT * FROM inquiries;
    """
    results = connectToMySQL(cls.db).query_db(query)
    inquiries = []
    for inquiry in results:
      inquiries.append(cls(inquiry))
    return inquiries
  
  @classmethod
  def view_one(cls, data):
    query = """
      SELECT * FROM inquiries WHERE id = %(id)s;
    """
    result = connectToMySQL(cls.db).query_db(query, data)
    return cls(result[0])
  
  @classmethod
  def delete_inquiry(cls, data):
    query = """
      DELETE FROM inquiries WHERE id = %(id)s;
    """
    return connectToMySQL(cls.db).query_db(query, data)
  
  @classmethod
  def view_one_with_user(cls, data):
    query = """
      SELECT * FROM inquiries 
      JOIN users ON inquiries.user_id = users.id
      WHERE inquiries.id = %(id)s;
      """
    result = connectToMySQL(cls.db).query_db(query, data)
    if len(result) < 1:
      return False
    inquiry = cls(result[0])
    for row in result:
      user_data = {
        'id': row['users.id'],
        'first_name' : row['users.first_name'],
        'last_name' : row['users.last_name'],
        'email': row['email'],
        'password' : None,
        'admin' : None, 
        'created_at' : row['users.created_at'],
        'updated_at' : row['updated_at']
      }
      inquiry.reporter = user_model.User(user_data)
    return inquiry

