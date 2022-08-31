import os
from urllib.parse import quote


mysql_host = os.environ.get("DB_HOST") or "db"
mysql_user = os.environ.get("DB_USER") or "root"
mysql_pass = os.environ.get("DB_PASS") or "root"
mysql_ddbb = os.environ.get("DB_NAME") or "dbticket"

SECRET_KEY = "oiewht;anbiwuehgads asdfa sdgfasdga 46836lyrul"
SQLALCHEMY_DATABASE_URI = f"mysql://{mysql_user}:{quote(mysql_pass)}@{mysql_host}:3306/{mysql_ddbb}"
SQLALCHEMY_TRACK_MODIFICATIONS = False