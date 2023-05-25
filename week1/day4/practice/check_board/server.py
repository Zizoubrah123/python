from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<int:x>/<int:i>/<color_one>/<color_two>')
def index(i,x,color_one,color_two):
    return render_template("index.html", row=x, col=i, color_one=color_one, color_two=color_two )



if __name__=="__main__":
    app.run(debug=True)