from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    PasswordField,
    TextAreaField,
    DateField,
    TimeField,
    IntegerField,
    BooleanField,
)
from wtforms.validators import DataRequired, Email, Length


class Ad_Event(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=40)])
    slug = StringField("Slug", validators=[DataRequired(), Length(max=20)])
    description = TextAreaField("Description")
    date = DateField("Selection date", format="%Y-%m-%d", validators=[DataRequired()])
    time = TimeField("Selection hour", format="%H-%M", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired(), Length(max=10)])
    category = StringField("Category", validators=[DataRequired(), Length(max=20)])
    max_attendess = IntegerField(
        "Maxium number of attendees", validators=[DataRequired()]
    )
