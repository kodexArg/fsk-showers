from flask import Flask
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from app.db import db
from app.views import crud


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object("app.config.DevelopmentConfig")

    db.init_app(app)
    Migrate(app, db)
    Bootstrap(app)

    return app


app = create_app()

# Blueprint register
app.register_blueprint(crud)
