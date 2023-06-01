from flask import Flask, render_template, redirect, request

from flask_app.models.dojos  import Dojo
from flask_app.models.ninjas  import Ninja

from flask_app import app 





@app.route("/create",methods=["POST"])
def show_ninja():
    print('------------------------------------', request.form)
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo_id'],
    }
    Ninja.save(data)
    return redirect("/dojos")





@app.route('/ninjas')
def call_dojo ():
    select = Dojo.Get_all()
    print ('-------------------select---',select)
    
    return render_template("ninjas.html", select=select)