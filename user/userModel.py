from controllers.dbController import *
from controllers.apiController import *

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("email", type=str, help="email of the user is required", required=True)
user_put_args.add_argument("password", type=str, help="password of the user is required", required=True)

user_resource_fields = {
    'id': fields.Integer,
    'email': fields.String,
    'password': fields.String,
}

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User(id = {self.id}, email = {self.email}, password = {self.password}"