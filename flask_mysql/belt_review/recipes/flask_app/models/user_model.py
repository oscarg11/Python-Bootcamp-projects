from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash #import flash
from flask_bcrypt import Bcrypt # import bcrypt
bcrypt = Bcrypt(app)
import re #import email regex
from flask_app.models import recipe_model

# email pattern validation
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# data-base schema name
db = "recipes_schema"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # stores all recipes that a single User instance has created
        self.recipe = []

    #(SAVE/INSERT USER)this method saves a user to our db and hash password
    @classmethod
    def save_user(cls, form_data):
        # hash password
        psword_hash = bcrypt.generate_password_hash(form_data['password'])
        user_data = {
        "first_name": form_data["first_name"],
        "last_name" : form_data["last_name"],
        "email" : form_data["email"],
        "password":psword_hash
        } 
        query = """
        INSERT INTO users ( first_name, last_name, email, password)
        VALUES ( %(first_name)s , %(last_name)s , %(email)s, %(password)s);
        """
        # user_data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(db).query_db( query, user_data)

    #(GET ONE USER) by id
    @classmethod
    def get_one_user(cls,data):
        query="SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL(db).query_db( query,data)
        print(result)
        one_user = cls(result[0])
        return one_user
    
    # (GET BY EMAIL)
    @classmethod
    def get_by_email(cls, data):
        query="SELECT * FROM users WHERE email=%(email)s;"
        result = connectToMySQL(db).query_db( query,data)
        print(result)
        if len(result)<1:
            return False
        user_email= cls(result[0])
        return user_email

    # REGISTRATION VALIDATION
    @staticmethod
    def validate_registration(form_data):
        is_valid = True
        if len(form_data['first_name']) < 2:
            flash("First name must be at least 2 characters!", "register")
            is_valid = False
        if form_data['first_name'].isalpha()==False:
            flash("First name must only consist of alphabetic characters", "register")
            is_valid = False
        if len(form_data['last_name']) < 2:
            flash("Last name must be at least 2 characters!", "register")
            is_valid = False
        if form_data['last_name'].isalpha()==False:
            flash("Last name must only consist of alphabetic characters", "register")
            is_valid = False
            # check if email is taken
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query, form_data)
        if len(results)>= 1:
            flash("Email already taken.","register")
            is_valid = False
        if not EMAIL_REGEX.match(form_data['email']):
            flash("Please enter a valid email!", "register")
            is_valid = False
        if form_data['password'] != form_data['conf_password']:
            flash("Passwords do not match","register")
        if len(form_data['password']) < 8:
            flash("Password must be at least 8 characters long!","register")
            is_valid = False
        return is_valid
    
    # LOGIN VALIDATION
    @staticmethod
    def validate_login(form_data):
        is_valid=True
        #Check if the email exists in the db 
        user_email={
            "email":form_data['email']
        }
        existing_user= User.get_by_email(user_email)
        if not existing_user:
            flash("Invalid email/password", "login")
            is_valid=False
        elif(existing_user):
            # check if password exists in db
            if not bcrypt.check_password_hash(existing_user.password, form_data['password']):
                flash("Invalid email/password", "login")
                is_valid=False
        return is_valid