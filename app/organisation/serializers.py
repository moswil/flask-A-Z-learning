from app import ma
from app.organisation.models import Organisation


class OrganisationSchema(ma.ModelSchema):

    class Meta:
        model = Organisation
        fields = ('id', 'name', 'domain', 'system_name',
                  'url', 'email_from', 'system_url')
        dump_only = ('id',)
