from app import rest_api

from app.users import api as users_api
from app.organisation import api as organisation_api


rest_api.add_resource(users_api.UserAPI, '/user')
rest_api.add_resource(users_api.UsersAPI, '/users')
rest_api.add_resource(users_api.AuthenticationAPI, '/authenticate')
rest_api.add_resource(users_api.VerifyEmailApi, '/verify-email')
# rest_api.add_resource(organisation_api.OrganisationApi, '/organisation')
