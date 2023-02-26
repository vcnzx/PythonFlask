# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
# model the class after the ninjas table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #? ===============GET ALL FROM NINJAS TABLE ===============
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        # Create an empty list to append our instances of ninjas
        ninjas = []
        # Iterate over the db results and create instances of users with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    #? =============CREATE A USER===========================
    @classmethod
    def save(cls, data ):
        query = """
            INSERT INTO ninjas ( first_name , last_name , age , created_at, updated_at, dojo_id ) 
            VALUES ( %(first_name)s , %(last_name)s , %(age)s , NOW() , NOW(), %(dojo_id)s );
        """
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db( query, data )