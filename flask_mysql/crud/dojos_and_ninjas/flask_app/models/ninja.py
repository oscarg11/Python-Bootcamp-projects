# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

db = "dojos_and_ninjas_schema"
class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #save/insert a ninja to the db
    @classmethod
    def save_ninja(cls, data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
        """
        result = connectToMySQL(db).query_db(query,data)
        return result

    #(GET ONE) This method will select only one ninja from the db by their id
    @classmethod
    def get_a_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])
    
    # (UPDATE) This method will edit/update a users info
    @classmethod
    def update_ninja(cls, data):
        query = """
        UPDATE ninjas
        SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(db).query_db(query,data)
    
    # (DELETE) This method will delete a ninja from the db
    @classmethod
    def delete_ninja(cls, data):
        query = """
        DELETE FROM ninjas
        WHERE id = %(id)s;
        """
        results = connectToMySQL(db).query_db(query,data)
        print("DELETE__", results)
        return results 