from .general_controller import GeneralController
from ..service import wifi_service


class WifiController(GeneralController):
    _service = wifi_service
