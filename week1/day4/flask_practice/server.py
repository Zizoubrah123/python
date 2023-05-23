from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', phrase="hello", times=5)

@app.route('/repeat/<string:banana>/<int:num>')
def repeat(banana, num):
    return render_template('index.html', banana=banana, num=num)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=6969)

