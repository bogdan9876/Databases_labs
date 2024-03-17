from .hotel_chain_service import HotelChainService
from .hotel_service import HotelService
from .user_service import UserService
from .hotel_location_service import HotelLocationService
from .review_service import ReviewService
from .room_service import RoomService
from .availability_service import AvailabilityService
from .registration_confirmation_service import RegistrationConfirmationService
from .fund_block_service import FundBlockService
from .reservation_service import ReservationService

hotel_chain_service = HotelChainService()
hotel_service = HotelService()
user_service = UserService()
hotel_location_service = HotelLocationService()
review_service = ReviewService()
room_service = RoomService()
availability_service = AvailabilityService()
registration_confirmation_service = RegistrationConfirmationService()
fund_block_service = FundBlockService()
reservation_service = ReservationService()
