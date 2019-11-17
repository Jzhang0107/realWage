from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    wage = StringField('Wage', validator = [DataRequired()])
    city1 = StringField('City 1', validator = [DataRequired()])
    city2 = StringField('City 2', validator = [DataRequired()])
    submit = SubmitField('Find')