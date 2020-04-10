import uuid
from flask import g


def make_code():
    return str(uuid.uuid4())
