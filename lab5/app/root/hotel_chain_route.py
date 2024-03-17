from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import hotel_chain_controller
from ..domain.hotel_chain import HotelChain

hotel_chain_bp = Blueprint('hotel_chain', __name__, url_prefix='/hotel_chain')


@hotel_chain_bp.get('')
def get_all_hotel_chains() -> Response:
    return make_response(jsonify(hotel_chain_controller.find_all()), HTTPStatus.OK)


@hotel_chain_bp.post('')
def create_hotel_chain() -> Response:
    content = request.get_json()
    hotel_chain = HotelChain.create_from_dto(content)
    hotel_chain_controller.create(hotel_chain)
    return make_response(jsonify(hotel_chain.put_into_dto()), HTTPStatus.CREATED)


@hotel_chain_bp.get('/<int:hotel_chain_id>')
def get_hotel_chain(hotel_chain_id: int) -> Response:
    return make_response(jsonify(hotel_chain_controller.find_by_id(hotel_chain_id)), HTTPStatus.OK)


@hotel_chain_bp.put('/<int:hotel_chain_id>')
def update_hotel_chain(hotel_chain_id: int) -> Response:
    content = request.get_json()
    hotel_chain = HotelChain.create_from_dto(content)
    hotel_chain_controller.update(hotel_chain_id, hotel_chain)
    return make_response("HotelChain updated", HTTPStatus.OK)


@hotel_chain_bp.patch('/<int:hotel_chain_id>')
def patch_hotel_chain(hotel_chain_id: int) -> Response:
    content = request.get_json()
    hotel_chain_controller.patch(hotel_chain_id, content)
    return make_response("HotelChain updated", HTTPStatus.OK)


@hotel_chain_bp.delete('/<int:hotel_chain_id>')
def delete_hotel_chain(hotel_chain_id: int) -> Response:
    hotel_chain_controller.delete(hotel_chain_id)
    return make_response("HotelChain deleted", HTTPStatus.OK)


@hotel_chain_bp.post('/generate-databases-via-cursor')
def generate_databases_via_cursor() -> Response:
    return make_response(jsonify(hotel_chain_controller.generate_databases_via_cursor()), HTTPStatus.OK)
