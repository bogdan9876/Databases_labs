from .general_controller import GeneralController
from ..service import hotel_chain_service


class HotelChainController(GeneralController):
    _service = hotel_chain_service
