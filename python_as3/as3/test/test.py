from datetime import datetime, timedelta
from flask import Flask, request
from werkzeug.datastructures import LanguageAccept
from flask.helpers import make_response
from flask.json import jsonify
import jwt

# create the Flask app
app = Flask(__name__)

@app.route('/protected')
def query_example():

    # if key doesn't exist, returns None
    language = request.args.get('language')

    return '''<h1>The language value is: {}</h1>'''.format(language)

@app.route('/login', methods=['GET'])
def login():

    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
    
        return jsonify({'token': token})
    
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

