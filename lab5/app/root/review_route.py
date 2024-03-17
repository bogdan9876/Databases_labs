from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import review_controller
from ..domain.review import Review

review_bp = Blueprint('review', __name__, url_prefix='/review')


@review_bp.route('', methods=['GET'])
def get_all_reviews() -> Response:
    return make_response(jsonify(review_controller.find_all()), HTTPStatus.OK)


@review_bp.route('', methods=['POST'])
def create_review() -> Response:
    content = request.get_json()
    review = Review.create_from_dto(content)
    review_controller.create(review)
    return make_response(jsonify(review.put_into_dto()), HTTPStatus.CREATED)


@review_bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id: int) -> Response:
    return make_response(jsonify(review_controller.find_by_id(review_id)), HTTPStatus.OK)


@review_bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id: int) -> Response:
    content = request.get_json()
    review = Review.create_from_dto(content)
    review_controller.update(review_id, review)
    return make_response("Review updated", HTTPStatus.OK)


@review_bp.route('/<int:review_id>', methods=['PATCH'])
def patch_review(review_id: int) -> Response:
    content = request.get_json()
    review_controller.patch(review_id, content)
    return make_response("Review updated", HTTPStatus.OK)


@review_bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id: int) -> Response:
    review_controller.delete(review_id)
    return make_response("Review deleted", HTTPStatus.OK)
