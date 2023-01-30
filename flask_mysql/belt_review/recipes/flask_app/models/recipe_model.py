from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask import flash #import flash

# data-base schema name
db = "recipes_schema"

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30_min = data['under_30_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.creator = None

    # (SAVE RECIPE)
    @classmethod
    def save_recipe(cls,data):

        query = """
        INSERT INTO recipes(name, description, instructions, date_made, under_30_min, user_id)
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30_min)s, %(user_id)s);
        """
        return connectToMySQL(db).query_db(query,data)
    
    # (UPDATE RECIPE)
    @classmethod
    def update_recipe(cls, data):
        query = """
        UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, under_30_min=%(under_30_min)s
        WHERE recipes.id = %(id)s;
        """
        return connectToMySQL(db).query_db(query,data)
    
    # (DELETE RECIPE)
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE recipes.id = %(id)s;"
        return connectToMySQL(db).query_db(query,data)
    
    # GET ONE RECIPE WITH A USER
    @classmethod
    def get_one_recipe_with_user(cls,data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        one_recipe = cls(results[0])

        user_data = {
                # Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                "id":results[0]['users.id'], 
                "first_name":results[0]['first_name'],
                "last_name":results[0]['last_name'],
                "email":results[0]['email'],
                "password":results[0]['password'],
                "created_at":results[0]['users.created_at'],
                "updated_at":results[0]['users.updated_at']
            }
        one_recipe.creator = user_model.User(user_data)
        return one_recipe
    

    # (GET USERS WITH RECIPES) associates users with their recipes
    @classmethod
    def get_all_recipes_with_creator(cls):
        # Get all recipes, and their one associated User that created it
        query = "SELECT * FROM recipes JOIN users ON users.id = recipes.user_id;"
        results = connectToMySQL(db).query_db(query)
        print(results)
        all_recipes = []
        for row in results:
            # Create a Post class instance from the information from each db row
            recipe_data ={
                "id":row['id'],
                "name":row['name'],
                "description":row['description'],
                "instructions":row['instructions'],
                "date_made":row['date_made'],
                "under_30_min":row['under_30_min'],
                "created_at":row['created_at'],
                "updated_at":row['updated_at'],
                "user_id":row['user_id']
            }
            # Prepare to make a User class instance, looking at the class in models/user.py
            user_data = {
                # Any fields that are used in BOTH tables will have their name changed, which depends on the order you put them in the JOIN query, use a print statement in your classmethod to show this.
                "id": row['users.id'], 
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            # Associate the Recipe class instance with the User class instance by filling in the empty creator attribute in the recipe class
            one_recipe = cls(recipe_data)
            # Create the User class instance that's in the user.py model file
            one_recipe.creator = user_model.User(user_data)
            # Append the Post containing the associated User to your list of Posts
            all_recipes.append(one_recipe)
        return all_recipes



    # RECIPE VALIDATION
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Recipe name must be at least 3 characters long.")
            is_valid = False
        if len(data['name']) == 0:
            flash("Recipe name cannot be blank")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be at least 3 characters long.")
            is_valid = False
        if len(data['description']) == 0:
            flash("Description cannot be blank")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Instructions must be at least 3 characters long.")
            is_valid = False
        if len(data['instructions']) == 0:
            flash("Instructions cannot be blank")
            is_valid = False
        if data['date_made'] == '':
            flash("A date is required.")
            is_valid = False
        if 'under_30_min' not in data :
            flash("Cook time is required. Please select Yes or No.")
            is_valid = False
        return is_valid
    