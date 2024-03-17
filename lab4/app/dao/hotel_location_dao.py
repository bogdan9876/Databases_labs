from .general_dao import GeneralDAO
from ..domain import HotelLocation


class HotelLocationDAO(GeneralDAO):
    _domain_type = HotelLocation
