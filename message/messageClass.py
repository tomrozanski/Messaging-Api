from message.messageModel import *
from auth.tokenMiddleware import *
import copy

class Message(Resource):
    @checkToken
    @marshal_with(resource_fields)
    def get(self, message_id, user_id):
        result = MessageModel.query.filter_by(id=message_id).first()
        if not result:
            abort(404, message="Could not find message with that id")
        
        resultBeforeUpdate = copy.copy(result)
        if result.read == False:
            result.read = True
            db.session.commit()
        return resultBeforeUpdate

    @checkToken
    @marshal_with(resource_fields)
    def delete(self, message_id, user_id):

        if message_id:
            result = MessageModel.query.filter_by(id=message_id).first()

            if result.sender_id == user_id or result.receiver_id == user_id:
                db.session.delete(result)
                db.session.commit()
                return '', 204

            if not result:
                abort(409, message="Sender or Receiver id not exists in message")
        
        abort(409, message="Missing message id")

