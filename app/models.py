from app.db import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    tickets = db.relationship("Ticket", backref="user")

    def __init__(self, username, role_id):
        self.username = username
        self.role_id = role_id

    def __repr__(self) -> str:
        return f"<User {self.usernmae}>"


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    users = db.relationship("User", backref="role")

    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f"<Role {self.name}>"


class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(60))
    lastname = db.Column(db.String(60))
    nationality = db.Column(db.String(60))
    tickets = db.relationship("Ticket", backref="client")

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self) -> str:
        return f"Client <{self.firstname} {self.lastname}>"


class Ticket(db.Model):
    ___tablename__ = "tickets"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    client_id = db.Column(db.Integer, db.ForeignKey("clients.id"))
    plan_id = db.Column(db.Integer, db.ForeignKey("plans.id"))

    def __init__(self, user_id, client_id, plan_id):
        self.user_id = user_id
        self.client__iid = client_id
        self.plan_id = plan_id

    def __repr__(self):
        return f"<Ticket {self.id}>"


class Plan(db.Model):
    __tablename__ = "plans"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    price = db.Column(db.Float())
    tickets = db.relationship("Ticket", backref="plan")

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"<Plan {self.name}>"
