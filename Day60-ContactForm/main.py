from flask import Flask, render_template, request
import requests

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
response = requests.get("https://api.npoint.io/4229128df8b9b655ba0e")
posts = response.json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    message_sent = False
    if request.method == "POST":
        message_sent = True
        name = request.form["name"].title()
        email = request.form["email"]
        phone = request.form["phone"]
        submission = request.form["message"]
        return render_template("contact.html", message_sent=message_sent, message=f"{name}, your message has been sent!")
    return render_template("contact.html", message_sent=message_sent)


@app.route("/form-entry", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        return render_template("contact.html", message="Your message has been sent successfully!")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
