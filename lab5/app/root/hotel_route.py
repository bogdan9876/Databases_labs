from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import hotel_controller
from ..domain.hotel import Hotel

hotel_bp = Blueprint('hotel', __name__, url_prefix='/hotel')


@hotel_bp.route('', methods=['GET'])
def get_all_hotels() -> Response:
    return make_response(jsonify(hotel_controller.find_all()), HTTPStatus.OK)


@hotel_bp.route('', methods=['POST'])
def create_hotel() -> Response:
    content = request.get_json()
    hotel = Hotel.create_from_dto(content)
    hotel_controller.create(hotel)
    return make_response(jsonify(hotel.put_into_dto()), HTTPStatus.CREATED)


@hotel_bp.route('/<int:hotel_id>', methods=['GET'])
def get_hotel(hotel_id: int) -> Response:
    return make_response(jsonify(hotel_controller.find_by_id(hotel_id)), HTTPStatus.OK)


@hotel_bp.route('/<int:hotel_id>', methods=['PUT'])
def update_hotel(hotel_id: int) -> Response:
    content = request.get_json()
    hotel = Hotel.create_from_dto(content)
    hotel_controller.update(hotel_id, hotel)
    return make_response("Hotel updated", HTTPStatus.OK)


@hotel_bp.route('/<int:hotel_id>', methods=['PATCH'])
def patch_hotel(hotel_id: int) -> Response:
    content = request.get_json()
    hotel_controller.patch(hotel_id, content)
    return make_response("Hotel updated", HTTPStatus.OK)


@hotel_bp.route('/<int:hotel_id>', methods=['DELETE'])
def delete_hotel(hotel_id: int) -> Response:
    hotel_controller.delete(hotel_id)
    return make_response("Hotel deleted", HTTPStatus.OK)
