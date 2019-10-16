from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class MemberDto:
    api = Namespace('member', description='Member related operations')
    member = api.model('member_details', {
        'user_id': fields.Integer(required=True, description='The user\'s Telegram ID'),
        'username': fields.String(required=True, description='The user\'s Telegram username'),
        'level': fields.Integer(required=False, description='The user\'s Language level,either 1,2 or 3 default is 0'),
        'role': fields.Integer(required=False, description='The user\'s role,2 for super admin,1 for teachers 0 for normal member; default 0'),
        'messages': fields.Integer(required=False, description='The number of messages sent by a user ;default is 0'),
    })