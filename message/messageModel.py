from controllers.dbController import *
from controllers.apiController import *

message_put_args = reqparse.RequestParser()
message_put_args.add_argument("subject", type=str, help="subject required", required=True)
message_put_args.add_argument("receiver_id", type=int, help="receiver_id required", required=True)
message_put_args.add_argument("creation_date", type=str, help="creation_date required", required=False)
message_put_args.add_argument("body", type=str, help="body required", required=True)

resource_fields = {
    'id': fields.Integer,
    'subject': fields.String,
    'sender_id': fields.Integer,
    'receiver_id': fields.Integer,
    'creation_date': fields.String,
    'body': fields.String,
    'read': fields.Boolean,
}

class MessageModel(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.String(30), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    body = db.Column(db.String(1000), nullable=False)
    read = db.Column(db.Boolean, default=False)

    sender = db.relationship("UserModel", foreign_keys=[sender_id])
    receiver = db.relationship("UserModel", foreign_keys=[receiver_id])

    def __repr__(self):
        return f"Message(subject = {self.subject}, creation_date = {self.creation_date}, sender_id = {self.sender_id}, " \
               f"receiver_id = {self.receiver_id}, body = {self.body}, read = {self.read})"

