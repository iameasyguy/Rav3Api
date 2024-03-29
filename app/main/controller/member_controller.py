from flask import request
from flask_restplus import Resource
from .. util.decorator import admin_token_required,token_required
from .. util.dto import MemberDto
from ..service.member_service import save_new_member,get_a_member,get_all_members,update_level


api = MemberDto.api
_member = MemberDto.member

@api.route('/')
class MemberList(Resource):
    @api.doc('list_of_all_members')
    @token_required
    @api.marshal_list_with(_member, envelope='data')
    def get(self):
        """List all registered members"""
        return get_all_members()

    @api.response(201, 'Member successfully created.')
    @api.doc('create a new member')
    @token_required
    @api.expect(_member, validate=True)
    def post(self):
        """Creates a new Member """
        data = request.json
        return save_new_member(data=data)



@api.route('/<user_id>')
@api.param('user_id', 'The Member identifier')
@api.response(404, 'Member not found.')
class Member(Resource):
    @api.doc('get a member')
    @token_required
    @api.marshal_with(_member)
    def get(self, user_id):
        """get a user given its identifier"""
        user = get_a_member(user_id)
        if not user:
            api.abort(404)
        else:
            return user


