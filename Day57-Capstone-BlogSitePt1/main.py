from flask import Flask, render_template
from post import posts_list

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=posts_list)


@app.route('/blog_post/<num>')
def blog_post(num):
    return render_template("post.html", all_posts=posts_list, num=int(num))


if __name__ == "__main__":
    app.run(debug=True)
