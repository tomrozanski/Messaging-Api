from message.messageModel import *
from datetime import datetime
from auth.tokenMiddleware import *

class Messages(Resource):
    @checkToken
    @marshal_with(resource_fields)
    def get(self, user_id):
        read = request.args.get("read")

        if not read:
            #All messages
            result = MessageModel.query.filter_by(sender_id=user_id).all()
        else:
            if read == 'False':
                read = False
            elif read == 'True':
                read = True
                
            #Read or Unread messages
            result = MessageModel.query.filter_by(sender_id=user_id, read=read).all()
        if not result:
            abort(404, message="Could not find message with that email")
        return result

    @checkToken
    @marshal_with(resource_fields)
    def post(self, user_id):
        args = message_put_args.parse_args()
        now = datetime.now()
        creation_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        
        message = MessageModel(subject=args['subject'], creation_date=creation_date, sender_id=user_id,
                               receiver_id=args['receiver_id'], body=args['body'], read=False)
        db.session.add(message)
        db.session.commit()
        return message, 201