from flask_app import app
from flask import render_tamplate, session, request, redirect
from flask_app.models.dojo import dojo

@app.route("/create_dojo", methods=["POST"])
def add_dojo ():
    dojo.create_dojo(request.form)
    return redirect("/dojo")
@pp.route("/dojo")
def index():
    all_dojo=dojo.show_dojo()
    return render_tamplate("index.html", all_dojo=all_dojo)
