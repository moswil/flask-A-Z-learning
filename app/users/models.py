from datetime import datetime

from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.utils.misc import make_code


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), nullable=False, default=True)
    is_deleted = db.Column(db.Boolean(), nullable=False, default=False)
    deleted_datetime_utc = db.Column(db.DateTime(), nullable=True)
    verified_email = db.Column(db.Boolean(), nullable=True)
    verify_token = db.Column(
        db.String(255), nullable=True, unique=True, default=make_code)

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def update_email(self, new_email):
        self.verified_email = False
        self.verify_token = make_code()
        self.email = new_email

    def delete(self):
        self.is_deleted = True
        self.deleted_datetime_utc = datetime.now()


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False,
                     unique=True, default='user_role')

    users = db.relationship('User', backref='role', lazy='dynamic')
