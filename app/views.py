##################################################
#
#   Author          : josuebrunel
#   Filename        :
#   Description     :
#   Creation Date   : 15-05-2015
#   Last Modified   : Fri 15 May 2015 10:13:54 PM CEST
#
##################################################
import flask
from app import app, db

@app.route('/new')
def new():
    """Create new user
    """
    return flask.jsonify({'name':'Josh'})
