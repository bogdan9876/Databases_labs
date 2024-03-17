from .general_service import GeneralService
from ..dao import hotel_dao


class HotelService(GeneralService):
    _dao = hotel_dao
