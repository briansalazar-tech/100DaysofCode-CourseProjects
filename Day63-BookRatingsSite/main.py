import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

load_dotenv()

ABS_PATH = os.getenv("ABS_PATH")
DB_PATH = ABS_PATH + "Day63-BookRatingsSite/books-reviews.db"


app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"

db = SQLAlchemy(model_class=Base)

db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()

# Flask routes
@app.route('/')
def home():

    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()

    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":

        book_title = request.form["bookname"]
        book_author = request.form["bookauthor"]
        book_rating = float(request.form["bookrating"])

        with app.app_context():
            new_book = Book(
                title=book_title,
                author=book_author,
                rating=book_rating,
            )
            
            db.session.add(new_book)
            db.session.commit()
        
        # book_entry = {
        #     "title": book_title,
        #     "author": book_author,
        #     "rating": book_rating
        # }
        # all_books.append(book_entry)
        print(all_books)
        return redirect(url_for("home"))
    
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)