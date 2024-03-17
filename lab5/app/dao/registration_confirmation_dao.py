from typing import List

import sqlalchemy

from .general_dao import GeneralDAO
from ..domain import RegistrationConfirmation


class RegistrationConfirmationDAO(GeneralDAO):
    _domain_type = RegistrationConfirmation

    def insert_rows(self):
        self._session.execute(sqlalchemy.text("CALL insert_rows()"), {})
        self._session.commit()
