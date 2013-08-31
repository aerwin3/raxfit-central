from flask import Blueprint, render_template, redirect, request
blueprint = Blueprint('classes', __name__, url_prefix="/classes")
from models.Class import Class, ClassType
from shared import db

@blueprint.route('/')
def index():
    classes = Class.query.all()
    return render_template("classes/index.html", classes=classes)

@blueprint.route('/new')
def new():
    class_types = ClassType.query.all()
    return render_template("classes/new.html", class_types=class_types)

@blueprint.route('/create', methods=['POST','PUT'])
def create():

    form = request.form
    new_class = Class(form['size'], form['wod'], form['class_type'])
    db.session.add(new_class)
    db.session.commit()
    return redirect('classes')

@blueprint.route('/delete/<id>')
def delete(id):
    deleting_class = Class.query.filter_by(id=id).first()
    db.session.delete(deleting_class)
    db.session.commit()
    return redirect('classes')

@blueprint.route('/edit/<id>', methods=["GET", "POST"])
def edit(id):
    class_types = ClassType.query.all()
    edit_class = Class.query.filter_by(id=id).first()
    if request.method == "GET":
        return render_template("classes/edit.html", editing_class=edit_class, class_types=class_types)
    else:
        edit_class.size = request.form['size']
        edit_class.wod = request.form['wod']
        edit_class.type_id = request.form['class_type']
        db.session.add(edit_class)
        db.session.commit()
        return redirect('classes')




