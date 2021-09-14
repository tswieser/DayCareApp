from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from app.models import School


class SchoolForm(FlaskForm):

    name = StringField('name', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
