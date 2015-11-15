from flask import Flask
from flask_sqlalchemy import SQLAlchemy

print "attribute __name__ is %s" % __name__

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from app import views, models
