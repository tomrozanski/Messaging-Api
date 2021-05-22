from controllers.apiController import *
from controllers.dbController import *
from user.usersClass import *
from message.messageClass import *
from message.messagesClass import *
from auth.login import *
from auth.tokenMiddleware import *
import os

if os.path.isfile('database.db'):
    print("db exist")
    print(os.urandom(24))
else:
    db.create_all()
    print("db created")


api.add_resource(Users, "/users/")
api.add_resource(Message, "/message/<int:message_id>/")
api.add_resource(Messages, "/messages/")
api.add_resource(Login, "/login/")

if __name__ == "__main__":
    app.run(debug=True)
