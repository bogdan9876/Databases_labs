from .general_service import GeneralService
from ..dao import room_dao


class RoomService(GeneralService):
    _dao = room_dao
