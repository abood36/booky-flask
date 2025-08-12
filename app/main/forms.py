from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=200)])
    author = StringField("Author", validators=[DataRequired(), Length(max=120)])
    description = TextAreaField("Description", validators=[Optional(), Length(max=2000)])
    rating = IntegerField("Rating (0-10)", validators=[Optional(), NumberRange(min=0, max=10)])
    submit = SubmitField("Save")

class DeleteForm(FlaskForm):
    submit = SubmitField("Delete")