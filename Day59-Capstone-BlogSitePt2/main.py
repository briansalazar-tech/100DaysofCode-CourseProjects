import requests
from flask import Flask, render_template

response = requests.get("https://api.npoint.io/4229128df8b9b655ba0e")
post_list = response.json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", all_posts=post_list)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:post_id>")
def get_post(post_id):
    for post in post_list:
        if post["id"] == post_id:
            return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)