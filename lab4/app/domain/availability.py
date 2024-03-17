from __future__ import annotations
from typing import Dict, Any
from app import db


class Availability(db.Model):
    __tablename__ = 'availability'
    id = db.Column(db.Integer, primary_key=True)
    booking_start_date = db.Column(db.Date, nullable=False)
    booking_end_date = db.Column(db.Date, nullable=False)
    guest_count = db.Column(db.Integer)
    is_weekend = db.Column(db.Boolean)
    Room_id = db.Column(db.Integer, db.ForeignKey('room.id'), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Availability({self.id}, '{self.booking_start_date}', '{self.booking_end_date}', {self.guest_count}, {self.is_weekend}, {self.Room_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'booking_start_date': self.booking_start_date.isoformat() if self.booking_start_date else None,
            'booking_end_date': self.booking_end_date.isoformat() if self.booking_end_date else None,
            'guest_count': self.guest_count,
            'is_weekend': self.is_weekend,
            'Room_id': self.Room_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Availability:
        availability = Availability(
            booking_start_date=dto_dict.get('booking_start_date'),
            booking_end_date=dto_dict.get('booking_end_date'),
            guest_count=dto_dict.get('guest_count'),
            is_weekend=dto_dict.get('is_weekend'),
            Room_id=dto_dict.get('Room_id')
        )
        return availability
