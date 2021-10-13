from flask import Blueprint, request
from ..models import Child, db

child_routes= Blueprint('children', __name__)

@child_routes.route('/children')
def get_parent_kids():
    all_children= Child.query.filter
