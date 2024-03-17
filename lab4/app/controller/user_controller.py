from .general_controller import GeneralController
from ..service import user_service


class UserController(GeneralController):
    _service = user_service
