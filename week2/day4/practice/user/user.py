from mysqlconnection import connectToMySQL
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def Get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('amazon').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name, last_name, email)
	    VALUES (%(first_name)s,%(last_name)s,%(email)s);"""
        result = connectToMySQL('amazon').query_db(query,data)
        print(result)
        return result