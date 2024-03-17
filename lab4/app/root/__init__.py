from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)
    from .hotel_chain_route import hotel_chain_bp
    from .hotel_route import hotel_bp
    from .hotel_location_route import hotel_location_bp
    from .user_route import user_bp
    from .review_route import review_bp
    from .room_route import room_bp
    from .availability_route import availability_bp
    from .registration_confirmation_route import registration_confirmation_bp
    from .fund_block_route import fund_block_bp
    from .reservation_route import reservation_bp
    app.register_blueprint(hotel_chain_bp)
    app.register_blueprint(hotel_bp)
    app.register_blueprint(hotel_location_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(room_bp)
    app.register_blueprint(availability_bp)
    app.register_blueprint(registration_confirmation_bp)
    app.register_blueprint(fund_block_bp)
    app.register_blueprint(reservation_bp)
