from flask import Blueprint, render_template
from models.Athlete import Athlete
blueprint = Blueprint('base', __name__, url_prefix="/")


@blueprint.route('/')
def index():
    return render_template("index.html")

