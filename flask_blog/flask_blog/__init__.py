from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '389106e0b2193996d6b690826ebf1dea'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flask_blog import routes

# Igor: I had to add this line to make sure flask had the application context in order
#   to run some commands from the commandline python.
app.app_context().push()