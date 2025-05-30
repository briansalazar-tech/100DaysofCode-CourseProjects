from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(message="Data is required"), Length(min=6, max=30), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(message="Data is required"), Length(min=8, max=30)])
    submit = SubmitField(label="Log in")


app = Flask(__name__)
app.secret_key = "supersecretkey"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    
    if login_form.validate_on_submit():
        username = (login_form.email.data)
        password = (login_form.password.data)
        if username == "admin@email.com" and password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    
    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
