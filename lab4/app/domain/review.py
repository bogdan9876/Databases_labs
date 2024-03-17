from __future__ import annotations
from typing import Dict, Any
from app import db


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    review_text = db.Column(db.String(1000))
    rating = db.Column(db.Float)
    visit_date = db.Column(db.Date)
    service_quality = db.Column(db.Enum('poor', 'average', 'good', 'excellent'))
    User_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'))

    def __repr__(self) -> str:
        return f"Review(id={self.id}, review_text='{self.review_text}', rating={self.rating}, " \
               f"visit_date={self.visit_date}, service_quality='{self.service_quality}', " \
               f"User_id={self.User_id}, Hotel_id={self.Hotel_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'review_text': self.review_text,
            'rating': self.rating,
            'visit_date': self.visit_date,
            'service_quality': self.service_quality,
            'User_id': self.User_id,
            'Hotel_id': self.Hotel_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Review:
        review = Review(
            review_text=dto_dict.get('review_text'),
            rating=dto_dict.get('rating'),
            visit_date=dto_dict.get('visit_date'),
            service_quality=dto_dict.get('service_quality'),
            User_id=dto_dict.get('User_id'),
            Hotel_id=dto_dict.get('Hotel_id')
        )
        return review
