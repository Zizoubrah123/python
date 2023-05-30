from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE
from flask_app.models.ninja import ninja
class dojo:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_name = data['dojo_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas_list=[]
    @classmethod
    #==============================================   create dojo   =================================================
    def create_dojo(cls,data):
        query = "INSERT INTO DOJOS (dojo_name) VALUES (%(dojo_name)s);"
        results= MySQLConnection(DATABASE).query_db(query, data)
        all_dojo = []
        for row in results:
            all_dojo.append(cls(row))
            return results
    #show all methods
    @classmethod
    def show_dojo(cls,data):
            query="SELECT * FROM dojos;"
            results_dojo = MySQLConnection(DATABASE).query_db(query, data)
            table_dojo=[]
            for row in results_dojo:
                table_dojo.append(cls(row))
            return table_dojo
    #read one dojo with ninjas
    @classmethod
    def show_ninja_in_dojo(cls,data):
        query="SELECT * FROM dojos JOIN ninjas on dojo.id=ninjas.dojo_id WHERE dojos.id=%(id)s  "
        results=MySQLConnection(DATABASE).query_db(query,data)
        ninjas=[]
        if results:
            this_dojo=cls(results[0])
            for row in results:
                data_test={
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
                
            }
                ninjas.append(ninja(data_test))
                return ninjas