from .general_dao import GeneralDAO
from ..domain import HotelChain


class HotelChainDAO(GeneralDAO):
    _domain_type = HotelChain
