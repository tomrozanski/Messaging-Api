from controllers.apiController import *
from user.userModel import *
from auth.jwtAuth import *

login_args = reqparse.RequestParser()
login_args.add_argument("email", type=str, help="email of the user is required", required=True)
login_args.add_argument("password", type=str, help="password of the user is required", required=True)

login_resource_fields = {
    'email': fields.String,
    'token': fields.String
}

class Login(Resource):
    @marshal_with(login_resource_fields)
    def post(self):
        args = login_args.parse_args()
        email = args.get("email")
        if email:
            result = UserModel.query.filter_by(email=email).first()

            if result:
                token = encode_auth_token(result.id)
                return {'email': email, 'token': token}, 200

        return 400
