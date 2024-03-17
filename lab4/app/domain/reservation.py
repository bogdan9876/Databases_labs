from __future__ import annotations
from typing import Dict, Any
from app import db


class Reservation(db.Model):
    __tablename__ = 'reservation'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum('confirmed', 'pending'), nullable=False)
    total_price = db.Column(db.Float)
    payment_method = db.Column(db.Enum('credit_card', 'debit_card', 'cash'))
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    FundBlock_id = db.Column(db.Integer, db.ForeignKey('fund_block.id'))

    def __repr__(self) -> str:
        return f"Reservation(id={self.id}, start_date={self.start_date}, end_date={self.end_date}, " \
               f"status='{self.status}', total_price={self.total_price}, payment_method='{self.payment_method}', " \
               f"User_id={self.User_id}, Room_id={self.Room_id}, FundBlock_id={self.FundBlock_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'status': self.status,
            'total_price': self.total_price,
            'payment_method': self.payment_method,
            'User_id': self.User_id,
            'Room_id': self.Room_id,
            'FundBlock_id': self.FundBlock_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Reservation:
        reservation = Reservation(
            start_date=dto_dict.get('start_date'),
            end_date=dto_dict.get('end_date'),
            status=dto_dict.get('status'),
            total_price=dto_dict.get('total_price'),
            payment_method=dto_dict.get('payment_method'),
            User_id=dto_dict.get('User_id'),
            Room_id=dto_dict.get('Room_id'),
            FundBlock_id=dto_dict.get('FundBlock_id')
        )
        return reservation
