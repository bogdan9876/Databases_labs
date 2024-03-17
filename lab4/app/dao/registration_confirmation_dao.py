from .general_dao import GeneralDAO
from ..domain import RegistrationConfirmation


class RegistrationConfirmationDAO(GeneralDAO):
    _domain_type = RegistrationConfirmation
