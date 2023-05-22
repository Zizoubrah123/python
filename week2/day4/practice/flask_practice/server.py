from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!!'

@app.route ('/dojo')
def dojo():
    return 'dojo!'

@app.route('/say/<string:flask>')
def flask(flask):
    return f'hi {flask}'

@app.route('/repeat/<string:banana>/<int:num>')
def repeat(banana, num):
    return f'{banana * num}'

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=6969)


if __name__=="__main__":# Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)

