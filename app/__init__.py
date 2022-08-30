from flask import Flask
from app.views import crud


app = Flask(__name__)
app.register_blueprint(crud)
