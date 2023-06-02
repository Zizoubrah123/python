from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
LETTRE_REGEX = re.compile(r'^[a-zA]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class log :
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name =data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod 
    def create(cls,data):
        query = """INSERT INTO log (first_name, last_name, email, password ) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
        """
        return connectToMySQL('validation').query_db(query,data)
    
    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if not LETTRE_REGEX.match(user['first_name']) and not LETTRE_REGEX.match(user['first_name']): 
            flash("must use only letters!")
        if len(user['first_name']) < 2:
            flash("first name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("last name must be at least 2 characters.")
            is_valid = False
        if not LETTRE_REGEX.match(user['email']): 
            flash("must use only letters!") 
        if len(user['email']) < 5:
            flash("email is unvalid.")
            is_valid = False
        if len(user['password']) < 3:
            flash("password must be at least 3 characters.")
            is_valid = False
        return is_valid


    @classmethod
    def get_by_email(cls,data):
        query = """
        SELECT * FROM log WHERE email = %(email)s;
        """
        result = connectToMySQL('validation').query_db(query,data)
        if(result):
            return cls(result[0]) # type: ignore
        return False