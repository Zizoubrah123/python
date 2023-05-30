from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/users')

@app.route("/users")
def index():
    users = User.Get_all()
    print(users)
    return render_template("index.html", all_users=users)

@app.route ("/user/new")
def new_user():
    return render_template("create_user.html")

@app.route('/create/user', methods=['POSt'])
def create():
    # print(request.form)
    User.save(request.form)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)