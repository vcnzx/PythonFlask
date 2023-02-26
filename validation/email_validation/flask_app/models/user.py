# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# model the class after the user table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

        #? =============SUBMIT EMAIL FORM===========================
    @classmethod
    def save(cls, data ):
        query = """
            INSERT INTO users ( email , created_at, updated_at ) 
            VALUES ( %(email)s , NOW() , NOW() );
        """
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def read(cls):
        query = """
            SELECT * FROM users
        """
        emails = []
        result = connectToMySQL(DATABASE).query_db(query)

        for row in result:
            emails.append(cls(row))
        return emails

    @staticmethod
    def validate(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash("EMAIL IS NOT VALID!")
            is_valid = False
        else:
            flash("The email address you entered is VALID")
        
        return is_valid

        pass