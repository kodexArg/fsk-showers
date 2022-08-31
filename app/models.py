from app.db import db


class TicketModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50))
    client = db.Column(db.String(50))
    plan_price = db.Column(db.String(50))

    def __init__(self, author, client, plan_price):
        self.author = author
        self.client = client
        self.plan_price = plan_price

    def __repr__(self):
       return f"<id {self.id}>"