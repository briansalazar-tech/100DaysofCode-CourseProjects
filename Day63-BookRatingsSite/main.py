from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

all_books = []

# Flask routes
@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_title = request.form["bookname"]
        book_author = request.form["bookauthor"]
        book_rating = request.form["bookrating"]
        
        book_entry = {
            "title": book_title,
            "author": book_author,
            "rating": book_rating
        }
        all_books.append(book_entry)
        print(all_books)
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)