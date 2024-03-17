from .general_controller import GeneralController
from ..service import registration_confirmation_service


class RegistrationConfirmationController(GeneralController):
    _service = registration_confirmation_service
