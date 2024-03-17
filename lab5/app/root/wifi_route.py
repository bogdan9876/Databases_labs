from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import wifi_controller
from ..domain.wifi import Wifi

wifi_bp = Blueprint('wifi', __name__, url_prefix='/wifi')

@wifi_bp.route('', methods=['GET'])
def get_all_wifi() -> Response:
    return make_response(jsonify(wifi_controller.find_all()), HTTPStatus.OK)


@wifi_bp.route('', methods=['POST'])
def create_wifi() -> Response:
    content = request.get_json()
    wifi = Wifi.create_from_dto(content)
    wifi_controller.create(wifi)
    return make_response(jsonify(wifi.put_into_dto()), HTTPStatus.CREATED)


@wifi_bp.route('/<int:wifi_id>', methods=['GET'])
def get_wifi(wifi_id: int) -> Response:
    return make_response(jsonify(wifi_controller.find_by_id(wifi_id)), HTTPStatus.OK)


@wifi_bp.route('/<int:wifi_id>', methods=['PUT'])
def update_wifi(wifi_id: int) -> Response:
    content = request.get_json()
    wifi = Wifi.create_from_dto(content)
    wifi_controller.update(wifi_id, wifi)
    return make_response("Wifi updated", HTTPStatus.OK)


@wifi_bp.route('/<int:wifi_id>', methods=['PATCH'])
def patch_wifi(wifi_id: int) -> Response:
    content = request.get_json()
    wifi_controller.patch(wifi_id, content)
    return make_response("Wifi updated", HTTPStatus.OK)


@wifi_bp.route('/<int:wifi_id>', methods=['DELETE'])
def delete_wifi(wifi_id: int) -> Response:
    wifi_controller.delete(wifi_id)
    return make_response("Wifi deleted", HTTPStatus.OK)
