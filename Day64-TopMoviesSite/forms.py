from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RateMovieForm(FlaskForm):

    # def __init__(self, cur_rating, cur_review):
    #     super().__init__()
    #     self.rating = cur_rating
    #     self.review = cur_review

    rating = StringField(
        label="Your rating out of 10. Ex. 7.5",
        validators=[DataRequired()],
    )
    review = StringField(
        label="Your review",
        validators=[DataRequired()]
    )
    submit = SubmitField("Update")