from .general_controller import GeneralController
from ..service import hotel_location_service


class HotelLocationController(GeneralController):
    _service = hotel_location_service
