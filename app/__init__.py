import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

print "attribute __name__ is %s" % __name__
print "basedir is: "+str(basedir)
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
