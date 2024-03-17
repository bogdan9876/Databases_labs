from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import room_controller
from ..domain.room import Room

room_bp = Blueprint('room', __name__, url_prefix='/room')


@room_bp.route('', methods=['GET'])
def get_all_rooms() -> Response:
    return make_response(jsonify(room_controller.find_all()), HTTPStatus.OK)


@room_bp.route('', methods=['POST'])
def create_room() -> Response:
    content = request.get_json()
    room = Room.create_from_dto(content)
    room_controller.create(room)
    return make_response(jsonify(room.put_into_dto()), HTTPStatus.CREATED)


@room_bp.route('/<int:room_id>', methods=['GET'])
def get_room(room_id: int) -> Response:
    return make_response(jsonify(room_controller.find_by_id(room_id)), HTTPStatus.OK)


@room_bp.route('/<int:room_id>', methods=['PUT'])
def update_room(room_id: int) -> Response:
    content = request.get_json()
    room = Room.create_from_dto(content)
    room_controller.update(room_id, room)
    return make_response("Room updated", HTTPStatus.OK)


@room_bp.route('/<int:room_id>', methods=['PATCH'])
def patch_room(room_id: int) -> Response:
    content = request.get_json()
    room_controller.patch(room_id, content)
    return make_response("Room updated", HTTPStatus.OK)


@room_bp.route('/<int:room_id>', methods=['DELETE'])
def delete_room(room_id: int) -> Response:
    room_controller.delete(room_id)
    return make_response("Room deleted", HTTPStatus.OK)
