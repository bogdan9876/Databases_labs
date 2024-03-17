from .general_dao import GeneralDAO
from ..domain import FundBlock


class FundBlockDAO(GeneralDAO):
    _domain_type = FundBlock
