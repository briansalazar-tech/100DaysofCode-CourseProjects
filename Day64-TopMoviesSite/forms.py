from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RateMovieForm(FlaskForm):

    rating = StringField(
        label="Your rating out of 10. Ex. 7.5",
        validators=[DataRequired()],
    )
    review = StringField(
        label="Your review",
        validators=[DataRequired()]
    )
    submit = SubmitField("Update")


class AddForm(FlaskForm):
    title = StringField(
        label="Movie Title",
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Add Movie")