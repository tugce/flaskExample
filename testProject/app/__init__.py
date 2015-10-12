from flask import Flask
from flask.ext.mail import Mail
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)
app.config.from_object('config')
mail = Mail(app)
from app import views
