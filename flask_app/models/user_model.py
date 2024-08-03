from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
  db = 'page_turners'
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.email = data['email']
    self.password = data['password']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @staticmethod
  def validate(data):
    is_valid = True
    # First name validation
    if len(data['first_name']) < 1:
      is_valid = False
      flash('First name is required.', 'reg')
    elif len(data['first_name']) < 2:
      is_valid = False
      flash('First name must be at least 2 characters.', 'reg')
    
    # Last name validation
    if len(data['last_name']) < 1:
      is_valid = False
      flash('Last name is required.', 'reg')
    elif len(data['last_name']) < 2:
      is_valid = False
      flash('Last name must be at least 2 characters.', 'reg')

    # Email validation
    if len(data['email']) < 1:
      is_valid = False
      flash('Email is required.', 'reg')
    elif not EMAIL_REGEX.match(data['email']):
      is_valid = False
      flash('Email must be in a valid format.', 'reg')
    else:
      potential_user = User.get_by_email({'email':data['email']})
      if potential_user:
        is_valid = False
        flash('Email is currently in use. Please try another email or log in.', 'reg')
        ##if dundermifflin is the domain then they are automatically admin 
    
    # Password validation
    if len(data['password']) < 1:
      is_valid = False
      flash('Please provide a password.', 'reg')
    elif data['password'] != data['confirm_password']:
      is_valid = False
      flash('Passwords do not match.', 'reg')

    return is_valid
  
  @classmethod
  def create(cls, data):
    query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
    """
    return connectToMySQL(cls.db).query_db(query, data)
  
  @classmethod
  def get_by_email(cls, data):
    query = """
        SELECT * FROM users
        WHERE email = %(email)s;
    """
    results = connectToMySQL(cls.db).query_db(query,data)
    if results:
      return cls(results[0])
    return False
  
  @classmethod
  def get_by_id(cls, data):
    query = """
        SELECT * FROM users
        WHERE id = %(id)s;
    """
    results = connectToMySQL(cls.db).query_db(query,data)
    if results:
      return cls(results[0])
    return False
