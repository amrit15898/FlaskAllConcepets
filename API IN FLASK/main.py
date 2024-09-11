from flask import Flask


app = Flask(__name__)


@app.route("/home")
def home_page():
    return "This is home page"

if __name__ == "__main__":
    app.run(port=8000, debug=True)
