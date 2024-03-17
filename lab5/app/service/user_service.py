from .general_service import GeneralService
from ..dao import user_dao


class UserService(GeneralService):
    _dao = user_dao
