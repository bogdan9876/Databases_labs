from .general_controller import GeneralController
from ..service import hotel_chain_service


class HotelChainController(GeneralController):
    _service = hotel_chain_service

    def generate_databases_via_cursor(self):
        self._service.generate_databases_via_cursor()
