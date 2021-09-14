from flask import Blueprint, request
from ..models import db, School
from app.forms import SchoolForm

school_routes = Blueprint('schools', __name__)


@school_routes.route('/api/school')
def get_schools():
    all_schools = School.query.all()
    return {'schools': [school.to_dict() for school in all_schools]}


@school_routes.route('/api/school', methods=['POST'])
def post_school():
    form = SchoolForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        school = School(
            name=form.name.data,
            location=form.location.data,
            description=form.description.data
        )
        db.session.add(school)
        db.session.commit()
        return school.to_dict()

    errorMessages = []
    for field in form.errors:
        for error in form.errors[field]:
            formattedErr = error[10:]
            formattedField = field.replace(
                '_', ' ').replace(' id', '').capitalize()
            errorMessages.append(f'{formattedField} {formattedErr}')
    return {'errors': errorMessages}
