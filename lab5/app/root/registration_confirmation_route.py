from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import registration_confirmation_controller
from ..domain.registration_confirmation import RegistrationConfirmation

registration_confirmation_bp = Blueprint('registration_confirmation', __name__, url_prefix='/registration_confirmation')

@registration_confirmation_bp.route('', methods=['GET'])
def get_all_registration_confirmations() -> Response:
    return make_response(jsonify(registration_confirmation_controller.find_all()), HTTPStatus.OK)


@registration_confirmation_bp.route('', methods=['POST'])
def create_registration_confirmation() -> Response:
    content = request.get_json()
    registration_confirmation = RegistrationConfirmation.create_from_dto(content)
    registration_confirmation_controller.create(registration_confirmation)
    return make_response(jsonify(registration_confirmation.put_into_dto()), HTTPStatus.CREATED)


@registration_confirmation_bp.route('/<int:registration_confirmation_id>', methods=['GET'])
def get_registration_confirmation(registration_confirmation_id: int) -> Response:
    return make_response(jsonify(registration_confirmation_controller.find_by_id(registration_confirmation_id)), HTTPStatus.OK)


@registration_confirmation_bp.route('/<int:registration_confirmation_id>', methods=['PUT'])
def update_registration_confirmation(registration_confirmation_id: int) -> Response:
    content = request.get_json()
    registration_confirmation = RegistrationConfirmation.create_from_dto(content)
    registration_confirmation_controller.update(registration_confirmation_id, registration_confirmation)
    return make_response("RegistrationConfirmation updated", HTTPStatus.OK)


@registration_confirmation_bp.route('/<int:registration_confirmation_id>', methods=['PATCH'])
def patch_registration_confirmation(registration_confirmation_id: int) -> Response:
    content = request.get_json()
    registration_confirmation_controller.patch(registration_confirmation_id, content)
    return make_response("RegistrationConfirmation updated", HTTPStatus.OK)


@registration_confirmation_bp.route('/<int:registration_confirmation_id>', methods=['DELETE'])
def delete_registration_confirmation(registration_confirmation_id: int) -> Response:
    registration_confirmation_controller.delete(registration_confirmation_id)
    return make_response("RegistrationConfirmation deleted", HTTPStatus.OK)


@registration_confirmation_bp.post('/insert-rows')
def insert_rows() -> Response:
    return make_response(jsonify(registration_confirmation_controller.insert_rows()), HTTPStatus.OK)
