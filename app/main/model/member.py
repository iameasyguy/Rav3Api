import datetime

from .. import db,flask_bcrypt

class Member(db.Model):
    __tablename__ = "members"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.UnicodeText)
    level = db.Column(db.Integer, default=0)
    role = db.Column(db.Integer, default=0)
    messages = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<User '{}'>".format(self.username)
