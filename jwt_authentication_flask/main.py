from flask import Flask, request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_jwt_extended import create_access_token,jwt_required ,get_jwt_identity, JWTManager


app = Flask(__name__)

app.config["SECRET_KEY"] = "SUPER-SECRET-KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)

class User(db.Model):
    """Model definition for User."""
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f"Username ==> {self.username}"

with app.app_context():
    db.create_all()

class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        if not username or not password:
            return {"message": "Missing username or password"}

        if User.query.filter_by(username=username).first():
            return {"message": "username with this name alread exist"}

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return {"message": "user created sucessfully"}
    
class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]    

        user = User.query.filter_by(username=username).first()
        if user and user.password==password:
            print("this condition is true")
            access_token = create_access_token(identity=user.id)

            return {"access token": access_token}, 401
        
        return {"message": "Invalid credentials"}

from flask import jsonify

class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        return jsonify({"message": "You have accessed the protected route"})


api.add_resource(UserRegistration, "/register")
api.add_resource(UserLogin, "/login")    
api.add_resource(ProtectedResource, "/secure")
    
if __name__=="__main__":
    app.run(debug=True)

