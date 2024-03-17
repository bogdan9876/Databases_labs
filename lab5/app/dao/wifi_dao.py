from .general_dao import GeneralDAO
from ..domain import Wifi


class WifiDAO(GeneralDAO):
    _domain_type = Wifi
