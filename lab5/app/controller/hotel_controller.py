from .general_controller import GeneralController
from ..service import hotel_service


class HotelController(GeneralController):
    _service = hotel_service
