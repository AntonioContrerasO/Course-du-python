from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email
import email_validator
from  flask_bootstrap import Bootstrap




class Form(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(),Email()])
    password = PasswordField(label='Password', validators=[DataRequired(),Length(min=8)])
    submit = SubmitField(label="Log In")


def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app


app = create_app()
app.secret_key = "putoputo"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
    form = Form(request.form)
    if request.method == 'POST':
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    else:
        print("GG")
    return render_template('login.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
