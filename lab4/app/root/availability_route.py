from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import availability_controller
from ..domain.availability import Availability

availability_bp = Blueprint('availability', __name__, url_prefix='/availability')


@availability_bp.route('', methods=['GET'])
def get_all_availabilities() -> Response:
    return make_response(jsonify(availability_controller.find_all()), HTTPStatus.OK)


@availability_bp.route('', methods=['POST'])
def create_availability() -> Response:
    content = request.get_json()
    availability = Availability.create_from_dto(content)
    availability_controller.create(availability)
    return make_response(jsonify(availability.put_into_dto()), HTTPStatus.CREATED)


@availability_bp.route('/<int:availability_id>', methods=['GET'])
def get_availability(availability_id: int) -> Response:
    return make_response(jsonify(availability_controller.find_by_id(availability_id)), HTTPStatus.OK)


@availability_bp.route('/<int:availability_id>', methods=['PUT'])
def update_availability(availability_id: int) -> Response:
    content = request.get_json()
    availability = Availability.create_from_dto(content)
    availability_controller.update(availability_id, availability)
    return make_response("Availability updated", HTTPStatus.OK)


@availability_bp.route('/<int:availability_id>', methods=['PATCH'])
def patch_availability(availability_id: int) -> Response:
    content = request.get_json()
    availability_controller.patch(availability_id, content)
    return make_response("Availability updated", HTTPStatus.OK)


@availability_bp.route('/<int:availability_id>', methods=['DELETE'])
def delete_availability(availability_id: int) -> Response:
    availability_controller.delete(availability_id)
    return make_response("Availability deleted", HTTPStatus.OK)
