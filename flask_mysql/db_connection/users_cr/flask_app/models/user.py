from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash


#model the class after the user table created in my database
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#use class methods to query our data base

# this methods selects all users in our db
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        #call the connectToMySQL function with the schema you are targeting 
        results = connectToMySQL('users_schema').query_db(query)
        # create an empty list to append our instances of users
        users = []
        # iterate over the db results and  create instances of friends with cls
        for user in results:
            users.append( cls(user) )
        return users

    #this method saves a user to our db
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email) VALUES ( %(fname)s , %(lname)s , %(email)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db( query, data)
    
    # this method selects only one user from the db by id
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users_schema').query_db(query, data)
        return cls(result[0])
    
    # this method will update a users info
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s WHERE id=%(id)s;"
        return connectToMySQL('users_schema').query_db( query, data)

    # this method will delete a user from the db
    @classmethod
    def delete(cls, data):
        query = """
        DELETE FROM users
        WHERE id = %(id)s;
        """
        results = connectToMySQL('users_schema').query_db(query,data)
        print("DELETE__", results)
        return results 

    #form validation to get clean/desired input
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['fname']) < 3:
            flash("First name must be at least 3 characters")
            is_valid = False
        if len(data['lname']) < 3:
            flash("Last name must be at least 3 characters")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Please enter a valid email")
            is_valid = False
        return is_valid
        

