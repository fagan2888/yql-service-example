##################################################
#
#   Author          : josuebrunel
#   Filename        : config.py
#   Description     :
#   Creation Date   : 15-05-2015
#   Last Modified   : Fri 15 May 2015 10:35:10 PM CEST
#
##################################################

import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:////"+basedir+"service.db"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')
