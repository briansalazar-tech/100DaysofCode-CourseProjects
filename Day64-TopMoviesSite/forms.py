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

class AddForm(FlaskForm):
    title = StringField(
        label="Movie Title",
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Add Movie")


# data = {'page': 1, 'results': [{'adult': False, 'backdrop_path': '/mFt3dvxKugYPgUQgV16M6K2nEtc.jpg', 'genre_ids': [35], 'id': 8363, 'original_language': 'en', 'original_title': 'Superbad', 'overview': 'Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry.', 'popularity': 12.6234, 'poster_path': '/ek8e8txUyUwd2BNqj6lFEerJfbq.jpg', 'release_date': '2007-08-17', 'title': 'Superbad', 'video': False, 'vote_average': 7.256, 'vote_count': 7540}, {'adult': False, 'backdrop_path': '/8pOpgNLDu6j6aU7uE8DncBdOhsx.jpg', 'genre_ids': [35], 'id': 424322, 'original_language': 'ru', 'original_title': 'Суперплохие', 'overview': 'Contemporary Moscow. Danya, a struggling actor, has just lost his girlfriend. His troubles soon multiply when his younger brother Dima shows up at his apartment with a friend who has a bullet in his stomach.', 'popularity': 0.5041, 'poster_path': '/g5WotpNk2YAbCSsQcd6jQDRaX7f.jpg', 'release_date': '2016-10-13', 'title': 'Superbad', 'video': False, 'vote_average': 3.2, 'vote_count': 4}, {'adult': False, 'backdrop_path': None, 'genre_ids': [35], 'id': 238955, 'original_language': 'en', 'original_title': 'Superbadazz', 'overview': 'Desperate for money Rodney and Leon start up a low budget strip club in Rodney s parents basement. The two friends run into a few problems though, from faulty strippers to nasty loan sharks, but their biggest problem might just be keeping the whole operation secret from Mom and Dad.', 'popularity': 0.1635, 'poster_path': '/2HKFknUtxs2ZS8bRJ64q0oAUFXY.jpg', 'release_date': '2008-07-29', 'title': 'Superbadazz', 'video': False, 'vote_average': 2.0, 'vote_count': 1}, {'adult': False, 'backdrop_path': '/7zeCBNXQRDgetNLhHfHEWQ8xOcD.jpg', 'genre_ids': [35], 'id': 38570, 'original_language': 'en', 'original_title': 'The 41–Year–Old Virgin Who Knocked Up Sarah Marshall and Felt Superbad About It', 'overview': "Follows Andy, who needs to hook up with a hottie, pronto, because he hasn't had sex in... well, forever - and his luck isn't the only thing that's hard. His equally horny teenage roommates also need it superbad, and with the help of their nerdy pal, McAnalovin' and his fake I.D., they may tap more than just a keg.", 'popularity': 0.8667, 'poster_path': '/cZeQktLjM9NMCtigex7pBPJx34h.jpg', 'release_date': '2010-06-08', 'title': 'The 41–Year–Old Virgin Who Knocked Up Sarah Marshall and Felt Superbad About It', 'video': False, 'vote_average': 3.931, 'vote_count': 144}], 'total_pages': 1, 'total_results': 4}
# Individual = {'adult': False, 'backdrop_path': '/mFt3dvxKugYPgUQgV16M6K2nEtc.jpg', 'genre_ids': [35], 'id': 8363, 'original_language': 'en', 'original_title': 'Superbad', 'overview': 'Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry.', 'popularity': 12.6234, 'poster_path': '/ek8e8txUyUwd2BNqj6lFEerJfbq.jpg', 'release_date': '2007-08-17', 'title': 'Superbad', 'video': False, 'vote_average': 7.256, 'vote_count': 7540}
# for data in data["results"]:
#     print(data["title"])
#     print(data["release_date"])
#     print("")