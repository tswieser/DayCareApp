from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ChildForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    age = StringField('age', validators=[DataRequired()])
    birthday = StringField('birthday', validators=[DataRequired()])
    profile_img_url = StringField('profile_img_url', validators=[DataRequired()])
    notes = StringField('notes')
