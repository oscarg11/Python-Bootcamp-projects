# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
#import Ninja class from our models
from .ninja import Ninja
from pprint import pprint

db = "dojos_and_ninjas_schema"
# model the class after the dojos table from our database
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # list of ninja instances
        self.ninjas = []

    # This methods selects all Dojos in our db
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        #call the connectToMySQL function with the schema you are targeting 
        results = connectToMySQL(db).query_db(query)
        # create an empty list to append our instances of dojos
        dojos = []
        # iterate over the db results and  create instances of dojo with cls
        for row in results:
            dojos.append( cls(row) )
        return dojos

    #This method will save/insert a new dojo to our db
    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos ( name ) VALUES ( %(name)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(db).query_db( query, data)
    
    # This method selects only one dojo from the db by id
    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])
    
    # This method will associate the Dojo class and the Ninja class together
    @classmethod
    def get_dojos_with_ninjas(cls , data):
        query = """
        SELECT * FROM dojos
        LEFT JOIN ninjas
        ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(db).query_db(query , data)
        #results will be a list of ninjas objects 
        dojo = cls( results[0] )
        for row_in_db in results:
            pprint(row_in_db)
            #if statements makes sure that a row isnt occupied by "none" if ninja does not exist
            if row_in_db['id'] == None:
                return dojo
        # Parse the ninja data to make instances of ninjas and add them into our list
            ninja_data = {
                "id": row_in_db['ninjas.id'],
                "first_name": row_in_db['first_name'],
                "last_name": row_in_db['last_name'],
                "age": row_in_db['age'],
                "created_at": row_in_db['ninjas.created_at'],
                "updated_at": row_in_db['ninjas.updated_at']
            }
            dojo.ninjas.append( Ninja ( ninja_data))
        return dojo