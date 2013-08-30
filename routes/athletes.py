from flask import Blueprint, render_template
from models.Athlete import Athlete
blueprint = Blueprint('athletes', __name__, url_prefix="/athletes")


@blueprint.route('/')
def index():
    athletes = Athlete.query.all()
    return render_template("athletes/index.html", athletes = athletes)

