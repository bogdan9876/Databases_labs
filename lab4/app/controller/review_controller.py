from .general_controller import GeneralController
from ..service import review_service


class ReviewController(GeneralController):
    _service = review_service
