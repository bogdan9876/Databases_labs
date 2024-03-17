from .general_dao import GeneralDAO
from ..domain import Hotel


class HotelDAO(GeneralDAO):
    _domain_type = Hotel
