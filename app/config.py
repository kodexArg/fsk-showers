import os
from urllib.parse import quote

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    mysql_host = os.environ.get("FLASK_RUN_HOST") or "localhost"
    mysql_user = os.environ.get("FLASK_DB_USER") or "root"
    mysql_pass = os.environ.get("FLASK_DB_PASSWORD") or "root"
    mysql_ddbb = os.environ.get("FLASK_NAME") or "dbticket"

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("FLASK_APP_SECRET_KEY") or "0#$xr189687lkjhjbnlzzc34555"
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{mysql_user}:{quote(mysql_pass)}@{mysql_host}/{mysql_ddbb}"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
