from __future__ import annotations
from typing import Dict, Any
from app import db


class HotelChain(db.Model):
    __tablename__ = 'hotel_chain'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100))
    established_year = db.Column(db.Integer)
    owner_name = db.Column(db.String(50))
    number_of_hotels = db.Column(db.Integer)
    hotels = db.relationship('Hotel', backref='hotel_chain')

    def __repr__(self) -> str:
        return f"HotelChain({self.id}, '{self.name}', '{self.location}', {self.established_year}, '{self.owner_name}', {self.number_of_hotels})"

    def put_into_dto(self) -> Dict[str, Any]:
        hotels = [hotel.put_into_dto() for hotel in self.hotels]
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'established_year': self.established_year,
            'owner_name': self.owner_name,
            'number_of_hotels': self.number_of_hotels,
            'hotels': hotels if hotels else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> HotelChain:
        hotel_chain = HotelChain(
            name=dto_dict.get('name'),
            location=dto_dict.get('location'),
            established_year=dto_dict.get('established_year'),
            owner_name=dto_dict.get('owner_name'),
            number_of_hotels=dto_dict.get('number_of_hotels')
        )
        return hotel_chain
