import sqlalchemy

from .general_dao import GeneralDAO
from ..domain import HotelChain


class HotelChainDAO(GeneralDAO):
    _domain_type = HotelChain

    def generate_databases_via_cursor(self):
        self._session.execute(sqlalchemy.text("CALL generate_databases_via_cursor()"), {})
        self._session.commit()
