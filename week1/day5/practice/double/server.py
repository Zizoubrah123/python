from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key="tetststgdkfij"
@app.route('/')
def index():
    if "answer" not in session :
        session ["answer"] = random.randint(1,3)
    return render_template("index.html")
@app.route("/guess", methods=['POST'])
def play ():
    session['guess']=int(request.form["number"])
    return  redirect ('/')

app.route('/reply')
def replay_ninja():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)