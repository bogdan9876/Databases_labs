USE booking;

INSERT INTO Hotel_Chain (name, location, established_year, owner_name, number_of_hotels) VALUES
('Marriott', 'New York, USA', 1927, 'Marriott Family', 7000),
('Hilton', 'Los Angeles, USA', 1919, 'Conrad Hilton', 6100),
('Hyatt', 'Chicago, USA', 1957, 'Jay Pritzker', 950),
('InterContinental', 'London, UK', 1946, 'Juan Abel', 210),
('Radisson', 'Minneapolis, USA', 1909, 'Curtis L. Carlson', 1400),
('Accor', 'Paris, France', 1967, 'Paul Dubrule', 4200),
('Four Seasons', 'Toronto, Canada', 1960, 'Isadore Sharp', 119),
('Shangri-La', 'Kowloon, Hong Kong', 1971, 'Robert Kuok', 101),
('Mandarin Oriental', 'Hong Kong', 1963, 'J. N. Lo', 33),
('The Ritz-Carlton', 'Boston, USA', 1983, 'William B. Johnson', 115);

INSERT INTO Hotel (name, address, contact_info, rating, HotelChain_id) VALUES
('Marriott Marquis', 'Broadway, New York, USA', '1234567890', 4.5, 1),
('Hilton Times Square', '42nd St, New York, USA', '0987654321', 4.3, 2),
('Hyatt Regency', 'Wacker Dr, Chicago, USA', '1122334455', 4.2, 3),
('InterContinental London', 'Park Lane, London, UK', '2233445566', 4.6, 4),
('Radisson Blu Aqua Hotel', 'Columbus Dr, Chicago, USA', '3344556677', 4.1, 5),
('Accor Sydney', 'George St, Sydney, Australia', '4455667788', 4.4, 6),
('Four Seasons Hotel Sydney', 'George St, Sydney, Australia', '5566778899', 4.7, 7),
('Shangri-La Hotel Paris', 'Avenue Iéna, Paris, France', '6677889900', 4.8, 8),
('Mandarin Oriental Barcelona', 'Passeig de Gràcia, Barcelona, Spain', '7788990011', 4.9, 9),
('The Ritz-Carlton Berlin', 'Potsdamer Platz, Berlin, Germany', '8899001122', 4.0, 10);

INSERT INTO Hotel_Location (country, city, street, postal_code, Hotel_id) VALUES
('USA', 'New York', 'Broadway', '10019', 1),
('USA', 'New York', '42nd St', '10036', 2),
('USA', 'Chicago', 'Wacker Dr', '60601', 3),
('UK', 'London', 'Park Lane', 'W1K 1BE', 4),
('USA', 'Chicago', 'Columbus Dr', '60601', 5),
('Australia', 'Sydney', 'George St', '2000', 6),
('Australia', 'Sydney', 'George St', '2000', 7),
('France', 'Paris', 'Avenue Iéna', '75116', 8),
('Spain', 'Barcelona', 'Passeig de Gràcia', '08007', 9),
('Germany', 'Berlin', 'Potsdamer Platz', '10785', 10);

INSERT INTO wifi (ssid, password, security_type, band, speed, signal_strength)
VALUES
('block1', 'password', 'WPA2', '2.4GHz', 50.0, 70.0),
('block2', '1111111111', 'WEP', '5GHz', 100.0, 80.0),
('block3', 'qwerty123', 'WPA3', '2.4GHz', 75.0, 90.0),
('block4', 'zxcvbnmasd', 'WPA2', '5GHz', 60.0, 85.0),
('block5', '88888888', 'WEP', '2.4GHz', 90.0, 95.0);

INSERT INTO User (name, email, password, role, date_of_birth, phone_number) VALUES
('John Doe', 'john.doe@example.com', 'password', 'client', '1990-05-15', '+1234567890'),
('Jane Doe', 'jane.doe@example.com', 'password', 'client', '1992-09-20', '+1987654321'),
('Admin User', 'admin@example.com', 'adminpass', 'administrator', '1985-03-10', '+1888888888'),
('Alice Smith', 'alice.smith@example.com', 'password', 'client', '1987-12-25', '+1777777777'),
('Bob Johnson', 'bob.johnson@example.com', 'password', 'client', '1988-07-08', '+1666666666'),
('Eve White', 'eve.white@example.com', 'password', 'client', '1986-01-30', '+1555555555'),
('Charlie Brown', 'charlie.brown@example.com', 'password', 'client', '1991-11-05', '+1444444444'),
('David Lee', 'david.lee@example.com', 'password', 'client', '1989-06-15', '+1333333333'),
('Grace Wilson', 'grace.wilson@example.com', 'password', 'client', '1995-04-18', '+1222222222'),
('Harry Davis', 'harry.davis@example.com', 'password', 'client', '1993-08-02', '+1111111111');

INSERT INTO Review (review_text, rating, visit_date, service_quality, User_id, Hotel_id) VALUES
('Great hotel!', 4.5, '2023-11-15', 'excellent', 1, 1),
('Excellent service.', 4.7, '2023-11-20', 'good', 2, 2),
('Wonderful experience!', 4.9, '2023-10-05', 'excellent', 4, 3),
('Perfect location.', 4.6, '2023-10-10', 'good', 3, 4),
('Highly recommended.', 4.8, '2023-10-25', 'excellent', 5, 5),
('Lovely staff.', 4.4, '2023-10-30', 'good', 6, 6),
('Clean and comfortable.', 4.3, '2023-11-01', 'average', 7, 7),
('Amazing views.', 4.5, '2023-11-05', 'excellent', 8, 8),
('Friendly atmosphere.', 4.2, '2023-11-10', 'good', 9, 9),
('Top-notch service.', 4.7, '2023-11-20', 'excellent', 10, 10);

INSERT INTO Room (room_type, price_per_night, room_size, bed_type, Hotel_id, Wifi_id) VALUES
('Deluxe Room', 200.00, 350.00, 'King', 1, 1),
('Standard Room', 150.00, 275.00, 'Queen', 2, 1),
('Suite', 250.00, 500.00, 'King', 3, 2),
('Superior Room', 180.00, 300.00, 'King', 4, 2),
('Penthouse Suite', 400.00, 750.00, 'King', 5, 3),
('Executive Room', 220.00, 400.00, 'King', 6, 3),
('Family Room', 170.00, 450.00, 'Queen', 7, 4),
('Ocean View Room', 280.00, 375.00, 'King', 8, 4),
('Studio', 210.00, 325.00, 'King', 9, 5),
('Double Room', 160.00, 300.00, 'Double', 10, 5);

INSERT INTO Availability (booking_start_date, booking_end_date, guest_count, is_weekend, Room_id) VALUES
('2023-11-01', '2023-11-30', 2, true, 1),
('2023-12-01', '2023-12-31', 2, false, 2),
('2023-11-01', '2023-11-30', 2, true, 3),
('2023-12-01', '2023-12-31', 2, false, 4),
('2023-11-01', '2023-11-30', 2, true, 5),
('2023-12-01', '2023-12-31', 2, false, 6),
('2023-11-01', '2023-11-30', 2, true, 7),
('2023-12-01', '2023-12-31', 2, false, 8),
('2023-11-01', '2023-11-30', 2, true, 9),
('2023-12-01', '2023-12-31', 2, false, 10);

INSERT INTO Registration_Confirmation (send_date, status, confirmation_code, expiration_date, User_id) VALUES
('2023-10-23', 'confirmed', 'ABCD1234', '2023-11-23', 1),
('2023-10-23', 'pending', 'EFGH5678', '2023-11-23', 2),
('2023-10-24', 'confirmed', 'IJKL9012', '2023-11-24', 3),
('2023-10-24', 'confirmed', 'MNOP3456', '2023-11-24', 4),
('2023-10-25', 'confirmed', 'QRST7890', '2023-11-25', 5),
('2023-10-25', 'pending', 'UVWX1234', '2023-11-25', 6),
('2023-10-26', 'confirmed', 'YZAB5678', '2023-11-26', 7),
('2023-10-26', 'confirmed', 'CDEF9012', '2023-11-26', 8),
('2023-10-27', 'confirmed', 'GHIJ3456', '2023-11-27', 9),
('2023-10-27', 'confirmed', 'KLMN7890', '2023-11-27', 10);

INSERT INTO Fund_Block (block_amount, block_date, release_date, status, User_id, RegistrationConfirmation_id) VALUES
(200.00, '2023-10-23', '2023-11-23', 'released', 1, 1),
(150.00, '2023-10-23', null, 'active', 2, 2),
(220.00, '2023-10-24', null, 'active', 3, 3),
(180.00, '2023-10-24', null, 'active', 4, 4),
(280.00, '2023-10-25', '2023-11-25', 'released', 5, 5),
(170.00, '2023-10-25', null, 'active', 6, 6),
(240.00, '2023-10-26', null, 'active', 7, 7),
(200.00, '2023-10-26', null, 'active', 8, 8),
(260.00, '2023-10-27', null, 'active', 9, 9),
(210.00, '2023-10-27', null, 'active', 10, 10);

-- Inserting data into Reservation
INSERT INTO Reservation (start_date, end_date, status, total_price, payment_method, User_id, Room_id, FundBlock_id) VALUES
('2023-11-01', '2023-11-30', 'confirmed', 4000.00, 'credit_card', 1, 1, 1),
('2023-12-01', '2023-12-31', 'pending', 3000.00, 'credit_card', 2, 2, 2),
('2023-11-01', '2023-11-30', 'confirmed', 5000.00, 'debit_card', 3, 3, 3),
('2023-12-01', '2023-12-31', 'confirmed', 4000.00, 'credit_card', 4, 4, 4),
('2023-11-01', '2023-11-30', 'pending', 5600.00, 'debit_card', 5, 5, 5),
('2023-12-01', '2023-12-31', 'confirmed', 3400.00, 'cash', 6, 6, 6),
('2023-11-01', '2023-11-30', 'confirmed', 4800.00, 'debit_card', 7, 7, 7),
('2023-12-01', '2023-12-31', 'confirmed', 4200.00, 'credit_card', 8, 8, 8),
('2023-11-01', '2023-11-30', 'confirmed', 5200.00, 'cash', 9, 9, 9),
('2023-12-01', '2023-12-31', 'confirmed', 4300.00, 'debit_card', 10, 10, 10);
