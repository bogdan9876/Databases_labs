from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import fund_block_controller
from ..domain.fund_block import FundBlock

fund_block_bp = Blueprint('fund_block', __name__, url_prefix='/fund_block')


@fund_block_bp.route('', methods=['GET'])
def get_all_fund_blocks() -> Response:
    return make_response(jsonify(fund_block_controller.find_all()), HTTPStatus.OK)


@fund_block_bp.route('', methods=['POST'])
def create_fund_block() -> Response:
    content = request.get_json()
    fund_block = FundBlock.create_from_dto(content)
    fund_block_controller.create(fund_block)
    return make_response(jsonify(fund_block.put_into_dto()), HTTPStatus.CREATED)


@fund_block_bp.route('/<int:fund_block_id>', methods=['GET'])
def get_fund_block(fund_block_id: int) -> Response:
    return make_response(jsonify(fund_block_controller.find_by_id(fund_block_id)), HTTPStatus.OK)


@fund_block_bp.route('/<int:fund_block_id>', methods=['PUT'])
def update_fund_block(fund_block_id: int) -> Response:
    content = request.get_json()
    fund_block = FundBlock.create_from_dto(content)
    fund_block_controller.update(fund_block_id, fund_block)
    return make_response("FundBlock updated", HTTPStatus.OK)


@fund_block_bp.route('/<int:fund_block_id>', methods=['PATCH'])
def patch_fund_block(fund_block_id: int) -> Response:
    content = request.get_json()
    fund_block_controller.patch(fund_block_id, content)
    return make_response("FundBlock updated", HTTPStatus.OK)


@fund_block_bp.route('/<int:fund_block_id>', methods=['DELETE'])
def delete_fund_block(fund_block_id: int) -> Response:
    fund_block_controller.delete(fund_block_id)
    return make_response("FundBlock deleted", HTTPStatus.OK)
