from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["UPLOAD_FOLDER"] = "uploads"

if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    # Handle non-existent folder (create it or raise an error)
    os.makedirs(app.config["UPLOAD_FOLDER"])  # Create the folder if needed
    print("Created uploads folder.")
else:
    print("Upload folder exists")

db = SQLAlchemy(app) 


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route("/uploads", methods=["POST"])
def uploads():
    if request.method == "POST":
        try:
            file = request.files["file"]
            if file:
                print(file)
                filename = file.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                print(filepath, "************8")
                obj = file.save(filepath)  
                new_file = File(filename=filename)
                print(f"the file objects is {obj}")

                db.session.add(new_file)
                db.session.commit()


        except Exception as e:
            print(f"the error is {e}")
            return f"Something went wrong ee {e}"
    return "Something went wrong e"

with app.app_context():
    db.create_all()
        

if __name__ == "__main__":
    app.run(debug=True)
