from flask import Blueprint, request
from flask_login import current_user
from ..models import Child, db

child_routes= Blueprint('children', __name__)

@child_routes.route('/children')
def get_parent_kids():
    all_children= Child.query.filter(Child.user_id == current_user).all()
    return {'children':[children.to_dict() for children in all_children]}



