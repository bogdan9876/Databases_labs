from .general_dao import GeneralDAO
from ..domain import Review


class ReviewDAO(GeneralDAO):
    _domain_type = Review
