from .general_dao import GeneralDAO
from ..domain import Availability


class AvailabilityDAO(GeneralDAO):
    _domain_type = Availability
