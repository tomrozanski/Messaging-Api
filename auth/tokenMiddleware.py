from controllers.apiController import *
from user.userModel import *
from auth.jwtAuth import *
    
def checkToken(functionToDecorate):
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
           abort(401, message="Missing token")

        user_id = decode_auth_token(token)
        if user_id:
            result = UserModel.query.filter_by(id=user_id).first()
            if result: 
                kwargs['user_id'] = result.id
            else:
                abort(404, message=" Could not find user with that id")

        else: 
            abort(401, message="Token invalid")

        return functionToDecorate(*args, **kwargs)

    return decorated
