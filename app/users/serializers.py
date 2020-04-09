from app import ma
from app.users.models import AppUser


class AppUserSchema(ma.ModelSchema):

    class Meta:
        model = AppUser
        # fields to expose
        fields = ("id", "username", "email", "password")
        load_only = ("password",)
        dump_only = ('id',)
