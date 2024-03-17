from .general_service import GeneralService
from ..dao import fund_block_dao


class FundBlockService(GeneralService):
    _dao = fund_block_dao
