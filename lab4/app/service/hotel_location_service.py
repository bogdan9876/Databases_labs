from .general_service import GeneralService
from ..dao import hotel_location_dao


class HotelLocationService(GeneralService):
    _dao = hotel_location_dao
