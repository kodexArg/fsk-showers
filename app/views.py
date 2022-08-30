from flask import Blueprint, render_template

crud = Blueprint('crud', __name__)


@crud.route('/')
def index():
    return render_template('index.html')


@crud.route('/about')
def about():
    return "About Here"
