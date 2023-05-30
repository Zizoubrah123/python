from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/users')
def new_user():
    return render_template('form.html')

@app.route('/users/add', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')



@app.route('/show')
def show_user():
    return render_template('show.html', name=session['username'], email=session['useremail'])

@app.route('/aziz')
def aaaaaa():
    return render_template('show.html')



if __name__=="__main__":
    app.run(debug=True)
