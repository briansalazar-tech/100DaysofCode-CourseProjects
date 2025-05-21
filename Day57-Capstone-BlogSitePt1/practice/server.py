import random
import datetime
import requests
from blogdata import data
from flask import Flask, render_template

GENDERIZE_API = "https://api.genderize.io"
AGIFY_API = "https://api.agify.io"
BLOG_API = "https://www.npoint.io/docs/c790b4d5cab58020d391"

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):

    parameters = {
        "name": name,
    }

    #Genderize API
    gender_response = requests.get(GENDERIZE_API, params=parameters)
    gender = gender_response.json()["gender"]

    # Agify API
    age_response = requests.get(AGIFY_API, params=parameters)
    age = age_response.json()["age"]

    return render_template("guess.html", name=name.title(), gender=gender, age=age)

@app.route('/blog/<num>')
def blog(num):
    all_posts = data
    return render_template("blog.html", posts=all_posts, num=int(num))

app.run(debug=True)