from .general_service import GeneralService
from ..dao import wifi_dao


class WifiService(GeneralService):
    _dao = wifi_dao
