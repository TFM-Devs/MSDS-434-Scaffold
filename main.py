#from flask import jsonify

#app = Flask(__name__)

#@app.route('/')
#def hello():
#    """Return a friendly HTTP greeting."""
#    return 'Hello I like to make AI Apps'

#@app.route('/name/<value>')
#def name(value):
#    value = {"value": value}
#    return jsonify(value)

#if __name__ == '__main__':
#    app.run(host='127.0.0.1', port=8080, debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello I like to make AI Apps'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
