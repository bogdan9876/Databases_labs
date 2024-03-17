from __future__ import annotations
from typing import Dict, Any
from app import db


class RegistrationConfirmation(db.Model):
    __tablename__ = 'registration_confirmation'
    id = db.Column(db.Integer, primary_key=True)
    send_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum('confirmed', 'pending'), nullable=False)
    confirmation_code = db.Column(db.String(20))
    expiration_date = db.Column(db.Date)
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f"RegistrationConfirmation(id={self.id}, send_date={self.send_date}, status='{self.status}', " \
               f"confirmation_code='{self.confirmation_code}', expiration_date={self.expiration_date}, " \
               f"User_id={self.User_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'send_date': self.send_date.isoformat() if self.send_date else None,
            'status': self.status,
            'confirmation_code': self.confirmation_code,
            'expiration_date': self.expiration_date.isoformat() if self.expiration_date else None,
            'User_id': self.User_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RegistrationConfirmation:
        registration_confirmation = RegistrationConfirmation(
            send_date=dto_dict.get('send_date'),
            status=dto_dict.get('status'),
            confirmation_code=dto_dict.get('confirmation_code'),
            expiration_date=dto_dict.get('expiration_date'),
            User_id=dto_dict.get('User_id')
        )
        return registration_confirmation
