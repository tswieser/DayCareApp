from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from app.models import Class


class ClassForm(FlaskForm):

    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
