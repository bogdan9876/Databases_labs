from .general_controller import GeneralController
from ..service import room_service


class RoomController(GeneralController):
    _service = room_service
