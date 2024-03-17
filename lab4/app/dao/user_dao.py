from .general_dao import GeneralDAO
from ..domain import User


class UserDAO(GeneralDAO):
    _domain_type = User
