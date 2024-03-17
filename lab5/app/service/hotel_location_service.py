from .general_service import GeneralService
from ..dao import hotel_location_dao


class HotelLocationService(GeneralService):
    _dao = hotel_location_dao

    def insert_into_hotel_location(self, country, city, street, postal_code, Hotel_id):
        self._dao.insert_into_hotel_location(country, city, street, postal_code, Hotel_id)
