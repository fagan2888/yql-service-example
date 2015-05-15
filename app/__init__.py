##################################################
#
#   Author          : josuebrunel
#   Filename        : __init__.py
#   Description     :
#   Creation Date   : 15-05-2015
#   Last Modified   : Fri 15 May 2015 10:11:26 PM CEST
#
##################################################

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

try:
    db.create_all()
except (Exception,) as e:
    print(e)


import views
