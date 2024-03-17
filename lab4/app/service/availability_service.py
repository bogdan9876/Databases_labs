from .general_service import GeneralService
from ..dao import availability_dao


class AvailabilityService(GeneralService):
    _dao = availability_dao
