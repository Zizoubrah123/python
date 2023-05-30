from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE
class ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.lsat_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #create ninja
        @classmethod
        def create_ninja(cls, data):
            query="INSERT INTO ninjas(first_name,last_name,dojo_id)VALUES(%(first_name)s,%(last_name)s,%(dojo_id)s)"
            return MySQLConnection(DATABASE.query_db(query,data))
    #raed ninjas
    @classmethod
    def get_all_ninja(cls):
        query="SELECT * FROM ninjas;"
        results=MySQLConnection(DATABASE).query_db(query)

        table_ninjas=[]
        for row in results :
            table_ninjas.append(cls(row))
        return table_ninjas