##################################################
#
#   Author          : josuebrunel
#   Filename        :
#   Description     :
#   Creation Date   : 15-05-2015
#   Last Modified   : Fri 15 May 2015 11:53:18 PM CEST
#
##################################################
import pdb
import json
import flask
from flask import request
from app import app, db

from models import User

@app.route('/get')
def select():
    """
    """
    if request.method == "GET":
        users = User.query.all()
        results = [ u.to_dict() for u in users ]
        return flask.jsonify({'count': len(results), 'result' : results})
    else:
        return flask.jsonify({'error':'Invalid method'})

@app.route('/new')
def new():
    """Create new user
    """
    if request.method == 'GET':
        params = request.args.to_dict()
        u = User(**params)
        db.session.add(u)
        db.session.commit()
        return flask.jsonify(**params)
    else:
        return flask.jsonify({'error':'Invalid method'})
