from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db import db
from app.forms import TicketForm
from app.models import TicketModel

# import logging

# logging.basicConfig(
#     level=logging.INFO, filename="temp.log", format="{message}", style="{", filemode="w"
# )

crud = Blueprint("crud", __name__)


@crud.route("/")
def index_view():
    return render_template("index.html")


@crud.route("/list")
def list_view():
    tks = TicketModel.query.all()
    return render_template("list.html", tks=tks)


@crud.route("/create", methods=["GET", "POST"])
def create_view():
    form = TicketForm()
    if form.validate_on_submit():
        new_record = TicketModel(
            author=request.form["author"],
            client=request.form["client"],
            plan_price=request.form["plan_price"],
        )
        db.session.add(new_record)
        db.session.commit()

        flash("Registro añadido satisfactoriamente.")

        return redirect(url_for("crud.list_view"))

    return render_template("create.html", form=form)


# DELETE
@crud.route("/delete/<int:id>")
def delete_view(id):
    record = TicketModel.query.get(id)
    db.session.delete(record)
    db.session.commit()
    flash("Registro eliminado.")
    return redirect(url_for("crud.list_view"))


@crud.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@crud.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
