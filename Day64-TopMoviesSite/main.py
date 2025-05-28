import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from forms import RateMovieForm, AddForm
import requests

load_dotenv()

TMDB_HEADERS = {
    "accept": "application/json",
    "Authorization": os.getenv("TMDB_BEARER")
}
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_IMG_URL = "https://image.tmdb.org/t/p/w500"
TMDB_MOVIE_ID_URL = "https://api.themoviedb.org/3/movie/"
ABS_PATH = os.getenv("ABS_PATH")
DB_PATH = ABS_PATH + "Day64-TopMoviesSite/instance/top-movies.db"

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)

with app.app_context():
    db.create_all()

# Add entry(s)
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )

# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movies = result.scalars()
    return render_template("index.html",movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        search_title = form.title.data

        parameters = {
            "query": search_title
        }

        response = requests.get(url=TMDB_SEARCH_URL, headers=TMDB_HEADERS, params=parameters)
        movie_list = response.json()["results"]
        print(movie_list)

        return render_template("select.html", movies=movie_list)

    return render_template("add.html", form=form)


@app.route("/find")
def find():
    movie_id = request.args.get("movie_id")
    movie_url= f"{TMDB_MOVIE_ID_URL}{movie_id}?language=en-US"
    response = requests.get(url=movie_url, headers=TMDB_HEADERS).json()

    title = response["title"]
    img_url = f"{TMDB_IMG_URL}{response["poster_path"]}"
    year = response["release_date"].split("-")[0]
    
    description = response["overview"]
    # If nullable set to True on table, db can be populated without these prepopulated
    rating = 0
    ranking = 0
    review = "N/A"

    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        rating=rating,
        ranking=ranking,
        review=review,
        img_url=img_url

    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("edit", id = new_movie.id))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    movie_id = request.args.get("id")
    current_movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    
    form = RateMovieForm()

    if form.validate_on_submit():
        updated_rating = form.rating.data
        updated_review = form.review.data
            
        # With app context removed as it was causing movie to not update
        current_movie.rating = float(updated_rating)
        current_movie.review = updated_review
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("edit.html", movie=current_movie, form=form)


@app.route("/delete", methods=["GET"])
def delete():
    movie_id = request.args.get("id")

    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
