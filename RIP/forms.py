from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class FilmForm(FlaskForm):
        title = StringField('Tytuł', validators=[DataRequired()])
        year = StringField('Rok', validators=[DataRequired()])
        director = StringField('Reżyser', validators=[DataRequired()])
        opis = TextAreaField('Opis')
        submit = SubmitField('Wprowadź')


# TodoForm = TodoFormula()
# validators=[DataRequired(), ])