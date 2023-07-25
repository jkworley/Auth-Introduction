from flask import request, make_response, jsonify, session

from config import app

from models import User

@app.route("/login", methods = ['POST'])
def login():

    '''
    1. Fetch username from client-side
    2. Use username to grab user from table
    3. Use user to set session's user_id (session['user_id'])
    4. Return successful or unsuccessful response
    '''

@app.route("/logout", methods = ['DELETE'])
def logout():

    '''
    1. Nullify session's user_id (session['user_id'])
    2. Return successful response
    '''

if __name__ == '__main__':
    app.run(port = 5555, debug = True)