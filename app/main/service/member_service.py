import datetime
import threading

from app.main import db
from app.main.model.member import Member


def save_new_member(data):
    member = Member.query.filter_by(user_id=data['user_id']).first()
    if not member:
        new_member = Member(
            user_id=data['user_id'],
            username=data['username'],
            created_date=datetime.datetime.utcnow()
        )
        save_changes(new_member)
        response_object = {
            'status': 'success',
            'message': 'Successfully created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists.',
        }
        return response_object, 409


INSERTION_LOCK = threading.RLock()


def get_all_members():
    return Member.query.all()

def get_a_member(user_id):
    return Member.query.filter_by(user_id=user_id).first()

def update_level(user_id,level):
    with INSERTION_LOCK:
        member =Member.query.filter_by(user_id=user_id).first()
        if member:
            member.level=level
            save_changes(member)
            response_object = {
                'status': 'success',
                'message': 'Successfully updated.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'User does not exists.',
            }
            return response_object, 409



def save_changes(data):
    db.session.add(data)
    db.session.commit()