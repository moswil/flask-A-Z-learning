from app import db
from app.organisation.models import Organisation


class OrganisationRepository:

    @staticmethod
    def get_by_domain(domain):
        return db.session.query(Organisation).filter(Organisation.domain == domain).one_or_none()

    @staticmethod
    def get_all():
        return db.session.query(Organisation).all()
