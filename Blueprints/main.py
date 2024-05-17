from flask import  Flask,redirect,url_for,render_template,request
from blueprints.helloworld.first_blueprint import helloworld_bp
from blueprints.calender.calender import calender_bp

app=Flask(__name__)
app.register_blueprint(helloworld_bp)
app.register_blueprint(calender_bp, url_prefix = "/calendar")

if __name__ == '__main__':

    app.run(port=5000,debug=True)