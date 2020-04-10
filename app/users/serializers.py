from app import ma
from app.users.models import User


class UserSchema(ma.ModelSchema):

    class Meta:
        model = User
        # fields to expose
        fields = ("id", "username", "email", "password_hash")
        load_only = ("password_hash",)
        dump_only = ('id',)
