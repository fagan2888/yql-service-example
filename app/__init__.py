##################################################
#
#   Author          : josuebrunel
#   Filename        : __init__.py
#   Description     :
#   Creation Date   : 15-05-2015
#   Last Modified   : Fri 15 May 2015 11:00:09 PM CEST
#
##################################################

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')

app.debug = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)

try:
    db.create_all()
except (Exception,) as e:
    print(e)


import views
