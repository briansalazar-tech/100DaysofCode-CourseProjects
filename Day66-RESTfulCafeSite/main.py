import os
from random import choice
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

load_dotenv()

ABS_PATH = os.getenv("ABS_PATH")
DB_PATH = ABS_PATH + "Day66-RESTfulCafeSite/instance/cafes.db"

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    # return dictionary output when class is called
    def to_dict(self):
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
##  Create dictionary within the route to be turned into JSON ##
# @app.route("/random", methods=["GET"])
# def get_random_cafe():
#     result = db.session.execute(db.select(Cafe))
#     all_cafes = result.scalars().all()
#     random_cafe = choice(all_cafes)
#     return jsonify(
#         cafe= {
#             "id": random_cafe.id,
#             "name": random_cafe.name,
#             "coffee_price": random_cafe.coffee_price,
#             "location": random_cafe.location,
#             "map_url": random_cafe.map_url,
#             "img_url": random_cafe.img_url,

#             "amenities": {
#                 "can_take_calls": random_cafe.can_take_calls,
#                 "has_sockets": random_cafe.has_sockets,
#                 "has_toilet": random_cafe.has_toilet,
#                 "has_wifi": random_cafe.has_wifi,
#                 "seats": random_cafe.seats,
#             }
#         }
#     )

## Calls the to_dict() method that is created inside the Cafe class to return dictionary data ##
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = choice(all_cafes)
    #Simply convert the random_cafe data record to a dictionary of key-value pairs. 
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    cafes = []
    for cafe in all_cafes:
        cafes.append(cafe.to_dict())
    return jsonify(cafes=cafes)

@app.route("/search")
def search_cafe():
    if request.args.get("loc"):
        location = request.args.get("loc").title()
        result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
        all_cafes = result.scalars().all()
        if all_cafes:
            cafes = []
            for cafe in all_cafes:
                cafes.append(cafe.to_dict())
            return jsonify(cafes)
        else:
            return jsonify(
                {"No results": "No cafes found for the location query"}
            ), 404 # 404 returns a 404 error code in conjunction with the JSON data that is displayed
    else:
        return "Search path requires loc parameter. Ex. /search?loc=london"

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        # Form data in this project submitted using Postman
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = bool(request.form.get("has_toilet")), # Bool required to convert input from str to bool
        has_wifi = bool(request.form.get("has_wifi")),
        has_sockets = bool(request.form.get("has_sockets")),
        can_take_calls = bool(request.form.get("can_take_calls")),
        coffee_price = request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(
        {"Success": "Cafe added to the Cafe database"}
    )

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
