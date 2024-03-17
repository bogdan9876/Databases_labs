from __future__ import annotations
from typing import Dict, Any
from app import db


class Wifi(db.Model):
    __tablename__ = 'wifi'
    id = db.Column(db.Integer, primary_key=True)
    ssid = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    security_type = db.Column(db.String(50))
    band = db.Column(db.String(50))
    speed = db.Column(db.Float)
    signal_strength = db.Column(db.Float)

    def __repr__(self) -> str:
        return f"Wifi({self.id}, '{self.ssid}', '{self.password}', '{self.security_type}', '{self.band}', {self.speed}, {self.signal_strength})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'ssid': self.ssid,
            'password': self.password,
            'security_type': self.security_type,
            'band': self.band,
            'speed': self.speed,
            'signal_strength': self.signal_strength
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Wifi:
        wifi = Wifi(
            ssid=dto_dict.get('ssid'),
            password=dto_dict.get('password'),
            security_type=dto_dict.get('security_type'),
            band=dto_dict.get('band'),
            speed=dto_dict.get('speed'),
            signal_strength=dto_dict.get('signal_strength'),
        )
        return wifi

