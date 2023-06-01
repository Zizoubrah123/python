from flask_app.config.mysqlconnection import connectToMySQL


class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def Get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('ninja_dojo').query_db(query)
        dojo = []
        for row in results:
            dojo.append(cls(row))
        print(dojo)
        return dojo


    @classmethod
    def create(cls,data):
        query="""INSERT INTO dojos(name)
                VALUES(%(name)s);"""
        
        return connectToMySQL('ninja_dojo').query_db(query,data)
    
    @classmethod
    def select_all(cls,data):
        query = """SELECT first_name,last_name,age,dojos.name FROM dojos JOIN ninjas ON ninjas.dojo_id =dojos.id WHERE dojos.id = %(id)s ;
        
        """
        results = connectToMySQL('ninja_dojo').query_db(query,data)
        ninjas=[]
        if results:
            
            for row in results :
                data={
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'name':row['name']                
                }
                
                ninjas.append(row)

        return ninjas
