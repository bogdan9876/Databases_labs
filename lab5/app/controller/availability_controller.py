from .general_controller import GeneralController
from ..service import availability_service


class AvailabilityController(GeneralController):
    _service = availability_service
