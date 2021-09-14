from flask import Blueprint, request
from ..models import Class, db
from app.forms import ClassForm


class_routes = Blueprint('classes', __name__)


@class_routes.route('/api/class/<int:id>')
def get_class(id):
    all_classes = Class.query.filter(Class.school_id == id).all()
    return{'classes': [classes.to_dict() for classes in all_classes]}


@class_routes.route('/api/class/<int:id>', methods=['POST'])
def post_class(id):
    form = ClassForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        classes = Class(
            name=form.name.data,
            description=form.description.data,
            school_id=id
        )
        db.session.add(classes)
        db.session.commit()

    errorMessages = []
    for field in form.errors:
        for error in form.errors[field]:
            formattedErr = error[10:]
            formattedField = field.replace(
                '_', ' ').replace(' id', '').capitalize()
            errorMessages.append(f'{formattedField} {formattedErr}')
    return {'errors': errorMessages}
