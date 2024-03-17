from .general_service import GeneralService
from ..dao import review_dao


class ReviewService(GeneralService):
    _dao = review_dao
