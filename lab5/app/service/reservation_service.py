from .general_service import GeneralService
from ..dao import reservation_dao


class ReservationService(GeneralService):
    _dao = reservation_dao
