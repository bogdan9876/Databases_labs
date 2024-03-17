from .general_dao import GeneralDAO
from ..domain import Room


class RoomDAO(GeneralDAO):
    _domain_type = Room
