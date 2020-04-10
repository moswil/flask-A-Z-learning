EMAIL_IN_USE = ({'message': 'User with that email already exists'}, 409)
USER_NAME_IN_USE = ({'message': 'User with that username already exists'}, 409)
UNAUTHORIZED = (
    {'message': 'Authentication is required to access this resource', 'type': 'UNAUTHORIZED'}, 401)
BAD_CREDENTIALS = (
    {'message': 'Incorrect username or password', 'type': 'BAD_CREDENTIALS'}, 401)
FORBIDDEN = ({'message': 'Access to this resource is forbidden'}, 403)
USER_DELETED = ({'message': 'This account has been deleted'}, 404)
EMAIL_NOT_VERIFIED = ({'message': 'The email address is not verified'}, 422)
