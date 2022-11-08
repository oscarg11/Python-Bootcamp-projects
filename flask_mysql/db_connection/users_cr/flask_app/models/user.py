#import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
#models the class after the users table in from our data base
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #Use a class method to query our database and put it into instances of the class
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
    #call the connectToMySQL function to the target schema
        results = connectToMySQL('users_schema').query_db(query)
        #empty list to append our instances of users
        users = []
        #iterate over the db results and create instances of users with cls
        for u in results:
            users.append(cls(u))
        return users 

    # class method to save a user to the data base
    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, created_at, updated_at) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW(), NOW() );"
        # data is a dictionary that will be passed into the save mehtod from server.py
        result = connectToMySQL('users_schema').query_db( query, data )
        return result
        
    # class method to select a particular user by id
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users_schema').query_db(query,data)
        return cls(result[0])
        
    #updates a users info
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"

        return connectToMySQL('users_schema').query_db(query,data) 
    #delets a user from the database
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)
