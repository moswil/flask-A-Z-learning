from app import ma
from app.users.models import User


class UserSchema(ma.ModelSchema):

    class Meta:
        model = User
        # fields to expose
        fields = ("id", "email", "firstname", "lastname", "password_hash")
        load_only = ("password_hash",)
        dump_only = ('id',)


class AuthenticateSchema(ma.ModelSchema):

    class Meta:
        model = User
        # fields to expose
        fields = ('id', 'email', 'password_hash')
        load_only = ("password_hash",)
        dump_only = ('id',)
