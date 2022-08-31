from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.forms import TicketForm
from app.models import TicketModel

crud = Blueprint("crud", __name__)


@crud.route("/")
def index_view():
    return render_template("index.html")


@crud.route("/create", methods=["GET", "POST"])
def create_view():
    form = TicketForm()
    if form.validate_on_submit():
        # writing form to database
        new_record = TicketModel(
            author=request.form["author"],
            client=request.form["client"],
            plan_price=request.form["plan_price"],
        )

        db.session.add(new_record)
        db.session.commit()

        return redirect(url_for("crud.create_view"))
    return render_template("create.html", form=form)


@crud.route("/update")
def update_view():
    return "update"


@crud.route("/delete")
def delete_view():
    return "delete"
