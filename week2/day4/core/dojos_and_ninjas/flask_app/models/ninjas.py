from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data["dojo_id"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # We create a list so that later we can add in all the burgers that are associated with a restaurant.

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO ninjas ( first_name, last_name , age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        return connectToMySQL('ninja_dojo').query_db( query, data)
    
    @classmethod
    def get_one(cls, data):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s;"
        # data = {'id':user_id}
        result = connectToMySQL('ninja_dojo').query_db(query, data)
        return result
    

    
    @classmethod
    def show_ninja_in_dojo(cls,data):
        query="""
                SELECT first_name,last_name,age,dojos.name FROM ninjas
                JOIN dojos on dojos.id=ninjas.dojo_id 
                WHERE dojos.id=%(id)s 
                """
        results=connectToMySQL('ninja_dojo').query_db(query,data)
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
