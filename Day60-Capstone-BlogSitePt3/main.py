import requests
import smtplib
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()

EMAIL_ADDRESS = os.getenv("TEST_EMAIL")
EMAIL_PASSWORD = os.getenv("TEST_EMAIL_APP_PW")

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

        email_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{submission}"
        
        # Send an email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL_ADDRESS,
                             password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=email,
                to_addrs=EMAIL_ADDRESS,
                msg=f"Subject:New Message from {name}\n\n{email_body}"
            )
            print("Email sent successfully!")

        return render_template("contact.html", message_sent=message_sent, message=f"{name}, your message has been sent!")
    return render_template("contact.html", message_sent=message_sent)


# Used to test form POST method. Once validated, functioanlity moved into contact route.
# @app.route("/form-entry", methods=["GET", "POST"])
# def receive_data():
#     if request.method == "POST":
#         return render_template("contact.html", message="Your message has been sent successfully!")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
