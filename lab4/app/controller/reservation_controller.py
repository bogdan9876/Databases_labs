from .general_controller import GeneralController
from ..service import reservation_service


class ReservationController(GeneralController):
    _service = reservation_service
