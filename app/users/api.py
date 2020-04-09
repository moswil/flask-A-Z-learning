from app import db, LOGGER

from flask import g, request, abort
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from app.users.serializers import AppUserSchema
from app.users.models import AppUser

from app.utils.errors import EMAIL_IN_USE, USER_NAME_IN_USE


def user_info(user, roles):
    pass


class UserAPI(Resource):
    app_user_schema = AppUserSchema()

    def get(self):
        # user = db.session.query(AppUser).filter(
        #     AppUser.id == g.current_user['id']).first()

        user = db.session.query(AppUser).filter(AppUser.id == 1).first()
        return self.app_user_schema.dump(user)

    def post(self):
        app_user = self.app_user_schema.load(request.get_json())

        db.session.add(app_user)

        try:
            db.session.commit()
            return self.app_user_schema.dump(app_user)
        except IntegrityError:
            LOGGER.error("email: {} already in use".format(app_user.email))
            return EMAIL_IN_USE


class AuthenticationAPI(Resource):
    pass


class UsersAPI(Resource):
    app_user_schema = AppUserSchema(many=True)

    def get(self):
        users = db.session.query(AppUser).all()
        return self.app_user_schema.dump(users)
