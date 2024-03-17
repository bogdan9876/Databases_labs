from .hotel_chain_dao import HotelChainDAO
from .hotel_dao import HotelDAO
from .hotel_location_dao import HotelLocationDAO
from .user_dao import UserDAO
from .review_dao import ReviewDAO
from .room_dao import RoomDAO
from .availability_dao import AvailabilityDAO
from .registration_confirmation_dao import RegistrationConfirmationDAO
from .fund_block_dao import FundBlockDAO
from .reservation_dao import ReservationDAO

availability_dao = AvailabilityDAO()
registration_confirmation_dao = RegistrationConfirmationDAO()
fund_block_dao = FundBlockDAO()
reservation_dao = ReservationDAO()
hotel_chain_dao = HotelChainDAO()
hotel_dao = HotelDAO()
hotel_location_dao = HotelLocationDAO()
user_dao = UserDAO()
review_dao = ReviewDAO()
room_dao = RoomDAO()
