##################################################
#
#   Author          : josuebrunel
#   Filename        : wsgi.py
#   Description     :
#   Creation Date   : 17-05-2015
#   Last Modified   : Sun 17 May 2015 07:21:23 AM CEST
#
##################################################

from app import app as application

if __name__ == '__main__':
    application.run()
