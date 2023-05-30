from flask_app import app
from flask import render_tamplate, session, request, redirect
from flask_app.models.dojo import dojo
from flask_app.models.ninja import ninja
@app.route('/ninjas')
def ninja():
    all_dojos=dojo.show_dojo()
    return render_tamplate("addNinja.html")
@app.route("/add_ninjas", methods=['POST'])
def add_new_ninja():
    session["first_name"]=request.form["first_name"]
    session["last_name"]=request.form["last_name"]
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'dojo_id':request.form['dojo_id']
    }
    ninja.create_ninja(data)
    return redirect('/ninjas')