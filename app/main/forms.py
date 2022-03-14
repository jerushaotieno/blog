from wtforms import SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

#Edit profile

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')