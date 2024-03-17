from __future__ import annotations
from typing import Dict, Any
from app import db


class HotelLocation(db.Model):
    __tablename__ = 'hotel_location'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(100))
    postal_code = db.Column(db.String(20))
    Hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"HotelLocation({self.id}, '{self.country}', '{self.city}', '{self.street}', '{self.postal_code}', {self.Hotel_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'country': self.country,
            'city': self.city,
            'street': self.street,
            'postal_code': self.postal_code,
            'Hotel_id': self.Hotel_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> HotelLocation:
        hotel_location = HotelLocation(
            country=dto_dict.get('country'),
            city=dto_dict.get('city'),
            street=dto_dict.get('street'),
            postal_code=dto_dict.get('postal_code'),
            Hotel_id=dto_dict.get('Hotel_id')
        )
        return hotel_location
