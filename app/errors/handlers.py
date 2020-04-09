from app import app
from flask import jsonify
from marshmallow import ValidationError


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400
