from flask import Flask, render_template, redirect, request

from flask_app.models.dojos  import Dojo
from flask_app.models.ninjas  import Ninja

from flask_app import app 

@app.route('/')
def main():
    return redirect('/dojos')

@app.route("/dojos")
def index():
    display =Dojo.Get_all()
    return render_template("index.html",display=display)

@app.route('/dojos', methods=['POSt'])
def create():
    Dojo.create(request.form)
    return redirect('/dojos')

@app.route("/dojo/<int:id>")
def show_one_by_id(id):
    data= { "id":id}
    
    result = Dojo.select_all(data)
    return render_template("display.ninja.html", result=result)

