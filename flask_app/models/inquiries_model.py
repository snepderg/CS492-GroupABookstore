from flask_app.config.mysqlconnection import connectToMySQL


class Inquiry:
  db = 'page_turners'
  def __init__(self,data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.category = data['category']
    self.description = data['description']
    self.user_id = data['user_id']
    self.reporter = None
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def create_inquiry(cls, data):
    query = """
      INSERT INTO inquiries (first_name, last_name, category, description, user_id)
      VALUES (%(first_name)s, %(last_name)s, %(category)s, %(description)s, %(user_id)s);
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

