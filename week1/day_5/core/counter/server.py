from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key="tetststgdkfij"

@app.route ('/')
def home():
    if "count" in session :
        session ["count"] += 1
    elif "count" not in session:
        session ["count"] = 1
    return render_template("index.html")



@app.route ('/destroy_session')
def destroy():
    session.clear()
    return redirect ('/')

if __name__=="__main__":
    app.run(debug=True)