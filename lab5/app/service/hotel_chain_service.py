from .general_service import GeneralService
from ..dao import hotel_chain_dao


class HotelChainService(GeneralService):
    _dao = hotel_chain_dao

    def generate_databases_via_cursor(self):
        self._dao.generate_databases_via_cursor()

