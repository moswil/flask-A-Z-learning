from app import db
from app.users.models import User

from sqlalchemy import func


class UserRepository:

    @staticmethod
    def get_by_id(user_id):
        return db.session.query(User).get(user_id).first()

    @staticmethod
    def get_by_email(email):
        return db.session.query(User).filter(func.lower(User.email) == func.lower(email)).first()

    @staticmethod
    def get_user_by_token(token):
        return db.session.query(User).filter(User.verify_token == token).first()
