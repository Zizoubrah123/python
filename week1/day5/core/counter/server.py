from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it safe'

@app.route('/', methods=['POST'] )
def counter():
    if 'key_name' in session:
        print('key exists!')
    else:
        print("key 'key_name' does NOT exist")

    return redirect("/dashboard ")

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['first_name']) < 3:
            flash("first name is required.")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("last name is required.")
            is_valid = False
        if int(data['calories']) < 200:
            flash("Calories must be 200 or greater.")
            is_valid = False
        if len(data['meat']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False




if __name__ == "__main__":
    app.run(debug=True)