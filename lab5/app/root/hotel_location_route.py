from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import hotel_location_controller
from ..domain.hotel_location import HotelLocation

hotel_location_bp = Blueprint('hotel_location', __name__, url_prefix='/hotel_location')


@hotel_location_bp.route('', methods=['GET'])
def get_all_hotel_locations() -> Response:
    return make_response(jsonify(hotel_location_controller.find_all()), HTTPStatus.OK)


@hotel_location_bp.route('', methods=['POST'])
def create_hotel_location() -> Response:
    content = request.get_json()
    hotel_location = HotelLocation.create_from_dto(content)
    hotel_location_controller.create(hotel_location)
    return make_response(jsonify(hotel_location.put_into_dto()), HTTPStatus.CREATED)


@hotel_location_bp.route('/<int:hotel_location_id>', methods=['GET'])
def get_hotel_location(hotel_location_id: int) -> Response:
    return make_response(jsonify(hotel_location_controller.find_by_id(hotel_location_id)), HTTPStatus.OK)


@hotel_location_bp.route('/<int:hotel_location_id>', methods=['PUT'])
def update_hotel_location(hotel_location_id: int) -> Response:
    content = request.get_json()
    hotel_location = HotelLocation.create_from_dto(content)
    hotel_location_controller.update(hotel_location_id, hotel_location)
    return make_response("HotelLocation updated", HTTPStatus.OK)


@hotel_location_bp.route('/<int:hotel_location_id>', methods=['PATCH'])
def patch_hotel_location(hotel_location_id: int) -> Response:
    content = request.get_json()
    hotel_location_controller.patch(hotel_location_id, content)
    return make_response("HotelLocation updated", HTTPStatus.OK)


@hotel_location_bp.route('/<int:hotel_location_id>', methods=['DELETE'])
def delete_hotel_location(hotel_location_id: int) -> Response:
    hotel_location_controller.delete(hotel_location_id)
    return make_response("HotelLocation deleted", HTTPStatus.OK)


@hotel_location_bp.post('/insert_into_hotel_location/<string:country>/<string:city>/<string:street>/<string'
                        ':postal_code>/<int'
                        ':Hotel_id>/')
def insert_into_hotel_location(country, city, street, postal_code, Hotel_id) -> Response:
    return make_response(jsonify(hotel_location_controller.insert_into_hotel_location(
        country, city, street, postal_code, Hotel_id)), HTTPStatus.OK)
