from .general_controller import GeneralController
from ..service import hotel_location_service


class HotelLocationController(GeneralController):
    _service = hotel_location_service

    def insert_into_hotel_location(self, country, city, street, postal_code, Hotel_id):
        self._service.insert_into_hotel_location(country, city, street, postal_code, Hotel_id)
