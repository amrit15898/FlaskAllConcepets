from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///formdata.db"
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class UserForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    age = StringField("age", validators=[InputRequired()] )
    address = StringField("address", validators=[InputRequired()])
    

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.String)
    address = db.Column(db.String)


@app.route("/", methods=["GET", "POST"])
def home_page():
    form = UserForm(request.form)
    if request.method=="POST":
        try:
            user = User(name=form.name.data, age=form.age.data, address=form.address.data)
            db.session.add(user)
            db.session.commit()
            form.name.data = ""
            form.age.data = ""
            form.address.data = ""
            return render_template("home.html", form=form)
        except Exception as e:
           print(e)
    return render_template("home.html", form=form)


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)