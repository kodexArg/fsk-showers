from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.views import crud


app = Flask(__name__)

app.config.from_object('app.config')
SQLAlchemy(app)

app.register_blueprint(crud)
