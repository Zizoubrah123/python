from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<int:num>/<color1>')
def hello_world(num, color):
    return render_template('index.html', num=num, color=color)

# @app.route('/play/<string:banana>/<int:num>')
# def repeat(banana, num):
#     return render_template('index.html','style.css', banana=banana, num=num)

if __name__ == "__main__":
    app.run(debug=True)
