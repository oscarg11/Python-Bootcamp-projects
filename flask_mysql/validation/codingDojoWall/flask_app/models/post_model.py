from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask import flash #import flash

# data-base schema name
db = "dojo_wall"

class Post:

    # data-base schema name
    db = "dojo_wall"

    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        # None can represent a currently empty space
        #  for a single User dictionary to be placed here,
        #  as a Tweet is made by ONE User. We want a User instance
        #  and all their attributes to be placed here,
        #  so something like data['...'] will not work as we have to make the User instance ourselves.
        self.creator = None
    
    # save a post
    @classmethod
    def save_post(cls,data):

        query = """
        INSERT INTO posts(content, user_id)
        VALUES (%(content)s, %(user_id)s);
            """
        return connectToMySQL(cls.db).query_db(query,data)

    #delete post(users can only delete their own posts)
    @classmethod
    def delete_post(cls, post_id):
        query = "DELETE FROM posts WHERE posts.id = %(id)s;"
        connectToMySQL(cls.db).query_db(query,{"id":post_id})
        return post_id

    # associate a User to Post
    @classmethod
    def get_all_posts_with_creator(cls):
        # Get all posts, and their one associated User that created it
        query = "SELECT * FROM posts JOIN users ON users.id = posts.user_id;"
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        all_posts = []
        for row in results:
            # Create a Post class instance from the information from each db row
            post_data ={
                "id":row['id'],
                "content":row['content'],
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
            # Associate the Post class instance with the User class instance by filling in the empty creator attribute in the Post class
            one_post = cls(post_data)
            # Create the User class instance that's in the user.py model file
            one_post.creator = user_model.User(user_data)
            # Append the Post containing the associated User to your list of Posts
            all_posts.append(one_post)
        return all_posts

    # Post Validation
    @staticmethod
    def validation_post(data):
        is_valid = True
        if len(data['content']) == 0:
            flash("Post cannot be blank!")
            is_valid = False
        return is_valid


