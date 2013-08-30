from flask import Blueprint, render_template
blueprint = Blueprint('classes', __name__, url_prefix="/classes")
from models.Class import Class

@blueprint.route('/')
def index():
    classes = Class.query.all()
    return render_template("classes/index.html", classes=classes)

