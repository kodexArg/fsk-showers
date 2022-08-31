from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Optional


def get_timestamp():
    return datetime.utcnow().timestamp()


class TicketForm(FlaskForm):
    author = StringField("Responsable", validators=[DataRequired()])
    client = StringField("Cliente", validators=[DataRequired()])
    plan_price = StringField("Plan", validators=[Optional()])
    timestamp = DateTimeField("Timestamp", default=get_timestamp())
    submit = SubmitField("Guardar")
