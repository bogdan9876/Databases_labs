from .general_service import GeneralService
from ..dao import registration_confirmation_dao


class RegistrationConfirmationService(GeneralService):
    _dao = registration_confirmation_dao
