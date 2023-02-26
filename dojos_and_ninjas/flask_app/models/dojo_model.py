# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.ninja_model import Ninja
# model the class after the dojos table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
        #? ===============GET ALL FROM DOJOS TABLE ===============
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # connectToMySQL function with DATABASE from __init__.py
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of users with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
            print(dojo)
        return dojos

    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = """
            SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id 
            WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db( query , data )
        # results will be a list of dojo objects with the ninja attached to each row. 
        dojo = cls( results[0] )
        dojo.ninjas = []
        for row_from_db in results:
            # Now we parse the ninja data to make instances of ninjas and add them into our list.
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"],
                "dojo_id" : row_from_db["dojo_id"]
            }
            new_ninja = Ninja(ninja_data)
            dojo.ninjas.append(new_ninja)
        return dojo


        #? =============CREATE A DOJO===========================
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db( query, data )