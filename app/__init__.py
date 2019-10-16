from flask_restplus import Api
from flask import Blueprint
from .main.controller.member_controller import api as member_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FORTUNA APP API',
          version='1.0',
          description='A fortuna web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(member_ns,path='/member')