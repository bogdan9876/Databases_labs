from __future__ import annotations
from typing import Dict, Any
from app import db


class FundBlock(db.Model):
    __tablename__ = 'fund_block'
    id = db.Column(db.Integer, primary_key=True)
    block_amount = db.Column(db.Float, nullable=False)
    block_date = db.Column(db.Date, nullable=False)
    release_date = db.Column(db.Date)
    status = db.Column(db.Enum('active', 'released'))
    RegistrationConfirmation_id = db.Column(db.Integer, db.ForeignKey('registration_confirmation.id'))
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    registration_confirmation = db.relationship("RegistrationConfirmation")

    def __repr__(self) -> str:
        return f"FundBlock(id={self.id}, block_amount={self.block_amount}, block_date={self.block_date}, " \
               f"release_date={self.release_date}, status='{self.status}', " \
               f"RegistrationConfirmation_id={self.RegistrationConfirmation_id}, User_id={self.User_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'block_amount': self.block_amount,
            'block_date': self.block_date.isoformat() if self.block_date else None,
            'release_date': self.release_date.isoformat() if self.release_date else None,
            'status': self.status,
            'RegistrationConfirmation_id': self.RegistrationConfirmation_id,
            'User_id': self.User_id,
            'registration_confirmation': self.registration_confirmation.put_into_dto() if self.registration_confirmation else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> FundBlock:
        fund_block = FundBlock(
            block_amount=dto_dict.get('block_amount'),
            block_date=dto_dict.get('block_date'),
            release_date=dto_dict.get('release_date'),
            status=dto_dict.get('status'),
            RegistrationConfirmation_id=dto_dict.get('RegistrationConfirmation_id'),
            User_id=dto_dict.get('User_id')
        )
        return fund_block
