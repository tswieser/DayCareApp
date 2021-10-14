from flask import Blueprint, request
from flask_login import current_user
from ..models import Child, db
from app.forms import ChildForm

child_routes= Blueprint('children', __name__)

@child_routes.route('/children')
def get_parent_kids():
    all_children= Child.query.filter(Child.user_id == current_user).all()
    return {'children':[children.to_dict() for children in all_children]}


@child_routes.route('/children', methods=['POST'])
def post_kid():
    form= ChildForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        children= Child(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            age=form.age.data,
            birthday=form.birthday.data,
            profile_img_url=form.profile_img_url.data,
            notes=form.notes.data,
            user_id=current_user
        )
