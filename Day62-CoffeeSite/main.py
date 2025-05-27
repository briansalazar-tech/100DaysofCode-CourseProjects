from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField(
        label="Cafe name", 
        validators=[DataRequired(message="Cafe name is required")]
        )
    
    location = StringField(
        label="Location URL",
        validators=[DataRequired(message="Location URL is required"), URL(message="Please enter a valid URL")]
        )
    
    open_time = StringField(
        label="Open Time Ex. 5:00AM",
        validators=[DataRequired(message="Opening time is required")]
    )

    closing_time = StringField(
        label="Closing Time Ex. 5:00PM",
        validators=[DataRequired(message="Closing time is required")]
    )

    coffee_rating = SelectField(
        label="Coffee Rating",
        choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], # Ussing symbol * number appends number on csv file
        validators=[DataRequired(message="Coffee rating is required")]
        )
    
    wifi_rating = SelectField(
        label="Wifi Rating",
        choices=["✘", "🛜", "🛜🛜", "🛜🛜🛜", "🛜🛜🛜🛜", "🛜🛜🛜🛜🛜"],
        validators=[DataRequired(message="WiFi rating is required")]
        )
    
    power_outlet_availability = SelectField(
        label="Power Outlet Availability", 
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired(message="Power outlet availability is required")]
        )
    
    submit = SubmitField('Submit')


# Flask routes
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("./Day62-CoffeeSite/cafe-data.csv", mode="a", encoding="utf-8") as csv_file:
            csv_file.write(
                f"\n{form.cafe.data},"
                f"{form.location.data},"
                f"{form.open_time.data},"
                f"{form.closing_time.data},"
                f"{form.coffee_rating.data},"
                f"{form.wifi_rating.data},"
                f"{form.power_outlet_availability.data}"
                )
            return redirect("cafes") # Redirect to cafes page after submission

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('./Day62-CoffeeSite/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows[0])
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
