from user.userModel import *

class Users(Resource):
    @marshal_with(user_resource_fields)
    def post(self):
        args = user_put_args.parse_args()
        email = args.get("email")
        result = UserModel.query.filter_by(email=email).first()
        if result:
            abort(409, message="Email is taken...")

        user = UserModel(email=args['email'], password=args['password'])
        db.session.add(user)
        db.session.commit()
        return user, 201