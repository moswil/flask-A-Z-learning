from app.organisation.repository import OrganisationRepository
from app import LOGGER
from flask import request
from werkzeug.exceptions import BadRequest


class OrganisationResolver:
    _cache = None

    @classmethod
    def _populate_cache(cls):
        LOGGER.info('Populating Organisation Cache')
        organisations = OrganisationRepository.get_all()

        cls._cache = {}
        for org in organisations:
            cls._cache[org.domain] = org

    @classmethod
    def resolve_from_domain(cls, domain):
        if not cls._cache:
            cls._populate_cache()

        if domain not in cls._cache:
            # Re-populate the cache and retry
            cls._populate_cache()
            LOGGER.warning(
                f'Could not resolve organisation from domain {domain}, trying to repopulate cache.')

            if domain not in cls._cache:
                LOGGER.error(
                    f'Could not resolve organisation from domain: {domain}, HTTP Origin: {request.environ.get("HTTP_ORIGIN", "")}, HTTP Referer: {request.environ.get("HTTP_REFERER", "")} ')

                raise BadRequest('Could not resolve organisation')

        return cls._cache[domain]
