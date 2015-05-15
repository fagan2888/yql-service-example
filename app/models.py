##################################################
#
#   Author          : josuebrunel
#   Filename        :
#   Description     :
#   Creation Date   : 15-05-2015
#   Last Modified   : Fri 15 May 2015 10:43:41 PM CEST
#
##################################################

from app import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32),index=True, unique=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.CHAR(1))
