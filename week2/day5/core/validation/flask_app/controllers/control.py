from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt        
from flask_app.modules.register import log
from flask_app import app 

bcrypt = Bcrypt(app)
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/dashboard')
def dashboarad():
    if not 'user_id' in session:  
        return redirect ('/')

    return render_template('dashboard.html')

@app.route('/create', methods=['POST'])
def create_user():
    if not log.validate_user(request.form):
        print("-----------------------------------",request.form)
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data ={
        **request.form,
        'password':pw_hash
    }
    user = log.create(data)
    session['user_id'] = user
    return redirect("/dashboard")

@app.route('/login', methods=['POST'])
def login():
    user_from_db = log.get_by_email({'email':request.form['email']})
    if(user_from_db):
        # check password
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        # if we get False after checking the password
            flash("Invalid Password", "Login")
            return redirect('/')
        session['user_id'] = user_from_db.id
        return redirect('/dashboard')
    flash("Invalid Email", "Login")
    return redirect('/')