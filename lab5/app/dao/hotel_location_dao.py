import sqlalchemy

from .general_dao import GeneralDAO
from ..domain import HotelLocation
from app import db


class HotelLocationDAO(GeneralDAO):
    _domain_type = HotelLocation

    def insert_into_hotel_location(self, country, city, street, postal_code, Hotel_id):
        self._session.execute(sqlalchemy.text("CALL insert_into_hotel_location(:country, :city, :street, "
                                              ":postal_code, :Hotel_id)"),
                              {"country": country, "city": city, "street": street,
                               "postal_code": postal_code, "Hotel_id": Hotel_id})
        self._session.commit()
