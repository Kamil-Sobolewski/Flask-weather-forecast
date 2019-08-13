from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LocationForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired(), Length(max=30)])
    submit = SubmitField('Get Forecast')
