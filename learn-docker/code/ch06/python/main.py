from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/colors')
def colors():
    return jsonify(['red', 'green', 'blue'])

if __name__ == '__main__':
    app.run()