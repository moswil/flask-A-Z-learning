from flask_restful import Resource
from flask import request, g

from app import LOGGER
from app.organisation.serializers import OrganisationSchema


class OrganisationApi(Resource):
    organisation_schema = OrganisationSchema(many=True)

    def get(self):
        return self.organisation_schema.dump(g.organisation)
