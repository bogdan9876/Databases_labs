from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import user_controller
from ..domain.user import User

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('', methods=['GET'])
def get_all_users() -> Response:
    return make_response(jsonify(user_controller.find_all()), HTTPStatus.OK)


@user_bp.route('', methods=['POST'])
def create_user() -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.create(user)
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id: int) -> Response:
    return make_response(jsonify(user_controller.find_by_id(user_id)), HTTPStatus.OK)


@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id: int) -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.update(user_id, user)
    return make_response("User updated", HTTPStatus.OK)


@user_bp.route('/<int:user_id>', methods=['PATCH'])
def patch_user(user_id: int) -> Response:
    content = request.get_json()
    user_controller.patch(user_id, content)
    return make_response("User updated", HTTPStatus.OK)


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int) -> Response:
    user_controller.delete(user_id)
    return make_response("User deleted", HTTPStatus.OK)
