from .hotel_controller import HotelController
from .hotel_chain_controller import HotelChainController
from .user_controller import UserController
from .hotel_location_controller import HotelLocationController
from .review_controller import ReviewController
from .room_controller import RoomController
from .availability_controller import AvailabilityController
from .registration_confirmation_controller import RegistrationConfirmationController
from .fund_block_controller import FundBlockController
from .reservation_controller import ReservationController
from .wifi_controller import WifiController

hotel_controller = HotelController()
hotel_chain_controller = HotelChainController()
user_controller = UserController()
hotel_location_controller = HotelLocationController()
review_controller = ReviewController()
room_controller = RoomController()
availability_controller = AvailabilityController()
registration_confirmation_controller = RegistrationConfirmationController()
fund_block_controller = FundBlockController()
reservation_controller = ReservationController()
wifi_controller = WifiController()
