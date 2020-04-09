from app import rest_api

from app.users import api as users_api


rest_api.add_resource(users_api.UserAPI, '/user')
rest_api.add_resource(users_api.UsersAPI, '/users')
