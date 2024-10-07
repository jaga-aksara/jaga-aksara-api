from wtforms import Form, FileField, validators
from flask_wtf import FlaskForm

class TranslatePegonScriptForm(FlaskForm):
    photo = FileField('photo', validators=[
            validators.Regexp(u'^.*\.(jpg|jpeg|png)$', message='Invalid file extension. Only image files with the following extensions are accepted: .jpg, .jpeg, and .png.')
        ])