import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

load_dotenv()

ABS_PATH = os.getenv("ABS_PATH")
DB_PATH = ABS_PATH + "Day67-Capstone-BlogSitePt3/instance/posts.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)


# New Post FOrm
class NewPostForm(FlaskForm):

    post_title = StringField(
        label="Blog Post Title",
        validators=[DataRequired()]
    )
    post_subtitle = StringField(
        label="Subtitle",
        validators=[DataRequired()]
    )
    post_author = StringField(
        label="Your name",
        validators=[DataRequired()]
    )
    post_bg_image = StringField(
        label="Blog Image URL",
        validators=[DataRequired(), URL()]
    )
    post_content = CKEditorField(
        label="Blog Content",
        validators=[DataRequired()]
    )
    submit = SubmitField(label="Submit Post")


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/show_post/<int:post_id>')
def show_post(post_id):
    print(post_id)
    request = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id))
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = request.scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/add_new_post", methods=["GET", "POST"])
def add_new_post():
    form = NewPostForm()
    if form.validate_on_submit():
        new_blog_post = BlogPost(
            title=form.post_title.data,
            subtitle=form.post_subtitle.data,
            date=date.today().strftime("%B %d, %Y"),
            author=form.post_author.data,
            img_url=form.post_bg_image.data,
            body=form.post_content.data,
        )
        db.session.add(new_blog_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)

# TODO: edit_post() to change an existing blog post

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete_post", methods=["GET"])
def delete_post():
    post_id = int(request.args.get("id"))
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
