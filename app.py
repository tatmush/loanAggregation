from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLLCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)
migrate=Migrate(app, db)
from views import *

if __name__ =='__main__':
	app.run()