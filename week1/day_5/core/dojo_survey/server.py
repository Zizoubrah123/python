from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key="tetststgdkfij"

@app.route("/")
def home():
    return render_template ("index.html")

@app.route('/processFrom' , methods=["POST"])
def create_page():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["section"] = request.form["section"]
    session["text"] = request.form["text"]
    return redirect('/result')

@app.route('/result')
def display():
    return render_template('result.html')


if __name__=="__main__":
    app.run(debug=True)