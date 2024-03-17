from http import HTTPStatus
from flask import Blueprint, Response, make_response

err_handler_bp = Blueprint('errors', __name__)


@err_handler_bp.app_errorhandler(HTTPStatus.NOT_FOUND)
def handle_404(error: int) -> Response:

    return make_response("Object not found", HTTPStatus.NOT_FOUND)


@err_handler_bp.app_errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
def handle_422(error: int) -> Response:

    return make_response("Input data is wrong or not full", HTTPStatus.UNPROCESSABLE_ENTITY)


@err_handler_bp.app_errorhandler(HTTPStatus.CONFLICT)
def handle_409(error: int) -> Response:

    return make_response("Such object is already exists in DB", HTTPStatus.CONFLICT)