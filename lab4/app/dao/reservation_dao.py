from .general_dao import GeneralDAO
from ..domain import Reservation


class ReservationDAO(GeneralDAO):
    _domain_type = Reservation
