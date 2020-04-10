from app import db, LOGGER

from flask import g, request, abort
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from app.users.serializers import UserSchema, AuthenticateSchema
from app.users.models import User
from app.users.repository import UserRepository as user_repository

from app.utils.emailer import send_mail
from app.utils.auth import admin_required, auth_required, generate_token
from app.utils.errors import (
    EMAIL_IN_USE, USER_NAME_IN_USE, USER_DELETED, EMAIL_NOT_VERIFIED, BAD_CREDENTIALS)


VERIFY_EMAIL_BODY = """
Dear {firstname} {lastname},

Thank you for creating a new {system} account. Please use the following link to verify your email address:

{host}/verifyEmail?token={token}

Kind Regards,
{organisation}
"""


def user_info(user, roles=None):
    return {
        'id': user.id,
        'token': str(generate_token(user)),
        'firstname': user.firstname,
        'lastname': user.lastname
    }


class UserAPI(Resource):
    user_schema = UserSchema()

    def get(self):
        # user = db.session.query(User).filter(
        #     User.id == g.current_user['id']).first()

        user = db.session.query(User).filter(User.id == 1).first()
        return self.user_schema.dump(user)

    def post(self):
        user = self.user_schema.load(request.get_json())

        db.session.add(user)

        try:
            db.session.commit()
        except IntegrityError:
            LOGGER.error("email: {} already in use".format(user.email))
            return EMAIL_IN_USE

        send_mail(recipient=user.email,
                  sender_name='Moses',
                  sender_email='moseswillfred1@gmail.com',
                  subject='Email Verification',
                  body_text=VERIFY_EMAIL_BODY.format(
                      firstname=user.firstname,
                      lastname=user.lastname,
                      system='Phren Test',
                      organisation='Phren Org',
                      host='phren.co.ke',
                      token=user.verify_token
                  ))
        LOGGER.debug(f"Sent verification email to {user.email}")

        return user_info(user), 201


class AuthenticationAPI(Resource):
    authenticate_schema = AuthenticateSchema()

    def post(self):
        user_data = self.authenticate_schema.load(request.get_json())

        user = user_repository.get_by_email(user_data.email)

        LOGGER.info(f'Authenticating user: {user_data.email}')

        if user:
            if user.is_deleted:
                LOGGER.debug(
                    f'Failed to authenticate, user {user_data.email} deleted')
                return USER_DELETED

            if not user.verified_email:
                LOGGER.debug(
                    f'Failed to authenticate, email {user_data.email} not verified')
                return EMAIL_NOT_VERIFIED
            if user.verify_password(user_data.password_hash):
                LOGGER.debug(
                    f'Successful authentication for email: {user_data.email}')
                return user_info(user)
        else:
            LOGGER.debug(f'User not found for {user_data.email}')
            return BAD_CREDENTIALS


class UsersAPI(Resource):
    users_schema = UserSchema(many=True)

    def get(self):
        users = db.session.query(User).all()
        return self.users_schema.dump(users)
