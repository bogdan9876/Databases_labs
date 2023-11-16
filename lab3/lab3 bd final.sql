CREATE DATABASE IF NOT EXISTS booking;
USE booking;

DROP TABLE IF EXISTS Reservation;
DROP TABLE IF EXISTS FundBlock;
DROP TABLE IF EXISTS RegistrationConfirmation;
DROP TABLE IF EXISTS Availability;
DROP TABLE IF EXISTS Room;
DROP TABLE IF EXISTS Review;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS HotelLocation;
DROP TABLE IF EXISTS Hotel;
DROP TABLE IF EXISTS HotelChain;

CREATE TABLE HotelChain (
id BIGINT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
location VARCHAR(100),
established_year YEAR,
owner_name VARCHAR(50),
number_of_hotels INT
) ENGINE = INNODB;

CREATE INDEX idx_location_established_year ON HotelChain(location, established_year);
CREATE INDEX idx_owner_hotels ON HotelChain(owner_name, number_of_hotels);

CREATE TABLE Hotel (
id BIGINT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
address VARCHAR(50) NOT NULL,
contact_info VARCHAR(250),
rating DECIMAL(3,2),
city VARCHAR(50),
country VARCHAR(50),
HotelChain_id BIGINT
) ENGINE = INNODB;

ALTER TABLE Hotel 
ADD CONSTRAINT FK_hotel_hotelchain
FOREIGN KEY (HotelChain_id)
REFERENCES HotelChain(id);

CREATE INDEX idx_name_address ON Hotel(name, address);
CREATE INDEX idx_city_country ON Hotel(city, country);

CREATE TABLE HotelLocation (
id BIGINT AUTO_INCREMENT PRIMARY KEY,
country VARCHAR(50) NOT NULL,
city VARCHAR(50) NOT NULL,
street VARCHAR(100),
postal_code VARCHAR(20),
Hotel_id BIGINT
) ENGINE = INNODB;

ALTER TABLE HotelLocation 
ADD CONSTRAINT FK_hotellocation_hotel
FOREIGN KEY (Hotel_id)
REFERENCES Hotel(id);

CREATE INDEX idx_country_city ON HotelLocation(country, city);
CREATE INDEX idx_street_postal ON HotelLocation(street, postal_code);

CREATE TABLE User (
id BIGINT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
password VARCHAR(50) NOT NULL,
role ENUM('client', 'administrator') NOT NULL,
date_of_birth DATE,
phone_number VARCHAR(15)
) ENGINE = INNODB;

CREATE INDEX idx_name_dob ON User(name, date_of_birth);
CREATE INDEX idx_email_phone ON User(email, phone_number);

CREATE TABLE Review (
id BIGINT AUTO_INCREMENT PRIMARY KEY,
review_text VARCHAR(1000),
rating DECIMAL(3,2),
visit_date DATE,
service_quality ENUM('poor', 'average', 'good', 'excellent'),
User_id BIGINT,
Hotel_id BIGINT
) ENGINE = INNODB;

ALTER TABLE Review 
ADD CONSTRAINT FK_review_user
FOREIGN KEY (User_id)
REFERENCES User(id),

ADD CONSTRAINT FK_review_hotel
FOREIGN KEY (Hotel_id)
REFERENCES Hotel(id);

CREATE INDEX idx_user_visit ON Review(User_id, visit_date);
CREATE INDEX idx_hotel_service ON Review(Hotel_id, service_quality);

CREATE TABLE Room (
id BIGINT AUTO_INCREMENT PRIMARY KEY,
room_type VARCHAR(50) NOT NULL,
price_per_night DECIMAL(10,2) NOT NULL,
room_size DECIMAL(5,2),
bed_type VARCHAR(50),
Hotel_id BIGINT
) ENGINE = INNODB;

ALTER TABLE Room 
ADD CONSTRAINT FK_room_hotel
FOREIGN KEY (Hotel_id)
REFERENCES Hotel(id);

CREATE INDEX idx_type_price ON Room(room_type, price_per_night);
CREATE INDEX idx_size_bed ON Room(room_size, bed_type);

CREATE TABLE Availability (
id BIGINT AUTO_INCREMENT PRIMARY KEY,
booking_start_date DATE NOT NULL,
booking_start_end DATE NOT NULL,
guest_count INT,
is_weekend BOOLEAN,
Room_id BIGINT
) ENGINE = INNODB;

ALTER TABLE Availability 
ADD CONSTRAINT FK_availability_room
FOREIGN KEY (Room_id)
REFERENCES Room(id);

CREATE INDEX idx_date_guest ON Availability(booking_start_date, guest_count);
CREATE INDEX idx_end_weekend ON Availability(booking_start_end, is_weekend);

CREATE TABLE RegistrationConfirmation (
id BIGINT AUTO_INCREMENT PRIMARY KEY,
send_date DATE NOT NULL,
status ENUM('confirmed', 'pending') NOT NULL,
confirmation_code VARCHAR(20),
expiration_date DATE,
User_id BIGINT
) ENGINE = INNODB;

ALTER TABLE RegistrationConfirmation 
ADD CONSTRAINT FK_registrationconfirmation_user
FOREIGN KEY (User_id)
REFERENCES User(id);

CREATE INDEX idx_senddate_status ON RegistrationConfirmation(send_date, status);
CREATE INDEX idx_code_expiration ON RegistrationConfirmation(confirmation_code, expiration_date);

CREATE TABLE FundBlock (
id BIGINT AUTO_INCREMENT PRIMARY KEY,
block_amount DECIMAL(10,2) NOT NULL,
block_date DATE NOT NULL,
RegistrationConfirmation_id BIGINT,
release_date DATE,
status ENUM('active', 'released'),
User_id BIGINT
) ENGINE = INNODB;

ALTER TABLE FundBlock 
ADD CONSTRAINT FK_fundblock_user
FOREIGN KEY (User_id)
REFERENCES User(id),

ADD CONSTRAINT FK_fundblock_registrationconfirmation
FOREIGN KEY (RegistrationConfirmation_id)
REFERENCES RegistrationConfirmation(id);

CREATE INDEX idx_blockdate_status ON FundBlock(block_date, status);
CREATE INDEX idx_release_user ON FundBlock(release_date, User_id);

CREATE TABLE Reservation (
id BIGINT AUTO_INCREMENT PRIMARY KEY,
start_date DATE NOT NULL,
end_date DATE NOT NULL,
status ENUM('confirmed', 'pending') NOT NULL,
total_price DECIMAL(10,2),
payment_method ENUM('credit_card', 'debit_card', 'cash'),
User_id BIGINT,
Room_id BIGINT,
FundBlock_id BIGINT
) ENGINE = INNODB;

ALTER TABLE Reservation 
ADD CONSTRAINT FK_reservation_user
FOREIGN KEY (User_id)
REFERENCES User(id),

ADD CONSTRAINT FK_reservation_room
FOREIGN KEY (Room_id)
REFERENCES Room(id),

ADD CONSTRAINT FK_reservation_fundblock
FOREIGN KEY (FundBlock_id)
REFERENCES FundBlock(id);

CREATE INDEX idx_startdate_status ON Reservation(start_date, status);
CREATE INDEX idx_price_payment ON Reservation(total_price, payment_method);

INSERT INTO HotelChain (name, location, established_year, owner_name, number_of_hotels) VALUES
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

INSERT INTO Hotel (name, address, contact_info, rating, city, country, HotelChain_id) VALUES 
('Marriott Marquis', 'Broadway, New York, USA', '1234567890', 4.5, 'New York', 'USA', 1),
('Hilton Times Square', '42nd St, New York, USA', '0987654321', 4.3, 'New York', 'USA', 2),
('Hyatt Regency', 'Wacker Dr, Chicago, USA', '1122334455', 4.2, 'Chicago', 'USA', 3),
('InterContinental London', 'Park Lane, London, UK', '2233445566', 4.6, 'London', 'UK', 4),
('Radisson Blu Aqua Hotel', 'Columbus Dr, Chicago, USA', '3344556677', 4.1, 'Chicago', 'USA', 5),
('Accor Sydney', 'George St, Sydney, Australia', '4455667788', 4.4, 'Sydney', 'Australia', 6),
('Four Seasons Hotel Sydney', 'George St, Sydney, Australia', '5566778899', 4.7, 'Sydney', 'Australia', 7),
('Shangri-La Hotel Paris', 'Avenue Iéna, Paris, France', '6677889900', 4.8, 'Paris', 'France', 8),
('Mandarin Oriental Barcelona', 'Passeig de Gràcia, Barcelona, Spain', '7788990011', 4.9, 'Barcelona', 'Spain', 9),
('The Ritz-Carlton Berlin', 'Potsdamer Platz, Berlin, Germany', '8899001122', 4.0, 'Berlin', 'Germany', 10);

INSERT INTO HotelLocation (country, city, street, postal_code, Hotel_id) VALUES 
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

INSERT INTO Room (room_type, price_per_night, room_size, bed_type, Hotel_id) VALUES 
('Deluxe Room', 200.00, 350.00, 'King', 1),
('Standard Room', 150.00, 275.00, 'Queen', 2),
('Suite', 250.00, 500.00, 'King', 3),
('Superior Room', 180.00, 300.00, 'King', 4),
('Penthouse Suite', 400.00, 750.00, 'King', 5),
('Executive Room', 220.00, 400.00, 'King', 6),
('Family Room', 170.00, 450.00, 'Queen', 7),
('Ocean View Room', 280.00, 375.00, 'King', 8),
('Studio', 210.00, 325.00, 'King', 9),
('Double Room', 160.00, 300.00, 'Double', 10);

INSERT INTO Availability (booking_start_date, booking_start_end, guest_count, is_weekend, Room_id) VALUES 
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

INSERT INTO RegistrationConfirmation (send_date, status, confirmation_code, expiration_date, User_id) VALUES 
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

INSERT INTO FundBlock (block_amount, block_date, release_date, status, User_id, RegistrationConfirmation_id) VALUES 
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

