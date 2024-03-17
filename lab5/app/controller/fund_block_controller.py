from .general_controller import GeneralController
from ..service import fund_block_service


class FundBlockController(GeneralController):
    _service = fund_block_service
