use booking;

# Трігери для третього пункту лаби

DROP TRIGGER IF EXISTS block_modification;
DELIMITER //
CREATE TRIGGER block_modification
BEFORE UPDATE
ON room FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Modification data in table is prohibited';
END //
DELIMITER ;

DROP TRIGGER IF EXISTS block_deletion;
DELIMITER //
CREATE TRIGGER block_deletion
BEFORE DELETE
ON user FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Delete data in table is prohibited';
END //
DELIMITER ;

DROP TRIGGER IF EXISTS minimal_cardinality;
DELIMITER //
CREATE TRIGGER minimal_cardinality
AFTER DELETE
ON hotel FOR EACH ROW
BEGIN
  IF(SELECT COUNT(*) FROM hotel)<6
  THEN SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Delete error minimal cardinality';
  END IF;
END //
DELIMITER ;

# Кінець трігерів для третього пункту (поставив це щоб легше було орієнтуватись)

# Трігери замість fk

DROP TRIGGER IF EXISTS wifi_id_connect1;
DELIMITER //
CREATE TRIGGER wifi_id_connect1
BEFORE INSERT
ON Room FOR EACH ROW
BEGIN
    IF NEW.Wifi_id NOT IN (SELECT id FROM Wifi)
    THEN SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid Wifi_id';
    END IF;
END //
DELIMITER ;

DROP TRIGGER IF EXISTS wifi_id_connect2;
DELIMITER //
CREATE TRIGGER wifi_id_connect2
BEFORE UPDATE
ON Room FOR EACH ROW
BEGIN
    IF NEW.Wifi_id NOT IN (SELECT id FROM Wifi)
    THEN SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid Wifi_id';
    END IF;
END //
DELIMITER ;

# Кінець трігерів які існують замість fk

# Користувацька функція разом з процедурою для її виклику

DROP FUNCTION IF EXISTS find_statistic;
DELIMITER //
CREATE FUNCTION find_statistic(operator VARCHAR(10))
RETURNS FLOAT DETERMINISTIC
BEGIN
    CASE operator
        WHEN 'MAX' THEN
            RETURN (SELECT MAX(block_amount) FROM fund_block);

        WHEN 'MIN' THEN
            RETURN (SELECT MIN(block_amount) FROM fund_block);

        WHEN 'SUM' THEN
            RETURN (SELECT SUM(block_amount) FROM fund_block);

        WHEN 'AVG' THEN
            RETURN (SELECT AVG(block_amount) FROM fund_block);

        ELSE
            RETURN NULL;

    END CASE;
END //
DELIMITER ;

DROP PROCEDURE IF EXISTS enter_operator;
DELIMITER //
CREATE PROCEDURE enter_operator(
    operator VARCHAR(10),
    OUT wanted_value FLOAT
)
BEGIN
    SET wanted_value = find_statistic(operator);
END //
DELIMITER ;

# Кінець користувацької функції та процедури для її виклику


# Процедура з використанням курсору (я вибрав ііi пункт)

DROP PROCEDURE IF EXISTS generate_databases_via_cursor;
DELIMITER //
CREATE PROCEDURE generate_databases_via_cursor()
BEGIN
    DECLARE done INT DEFAULT false;
    DECLARE database_name CHAR(50) DEFAULT "";
    DECLARE tables_amount INT;
    DECLARE counter INT DEFAULT 1;
    DECLARE main_cursor CURSOR FOR SELECT owner_name FROM hotel_chain;
    DECLARE CONTINUE HANDLER
    FOR NOT FOUND SET done = true;
    OPEN main_cursor;
    main_loop: LOOP
        FETCH main_cursor INTO database_name;
        IF done THEN
            LEAVE main_loop;
        END IF;
        SET @drop_databases_if_exists = CONCAT('DROP DATABASE IF EXISTS `', database_name , '`');
        PREPARE drop_databases FROM @drop_databases_if_exists;
        EXECUTE drop_databases;
        DEALLOCATE PREPARE drop_databases;

        SET @create_databases = CONCAT('CREATE DATABASE IF NOT EXISTS `', database_name, '`');
        PREPARE create_databases FROM @create_databases;
        EXECUTE create_databases;
        DEALLOCATE PREPARE create_databases;

        SET tables_amount = CEIL(RAND() * 9);
        SET counter = 1;
        WHILE counter <= tables_amount DO
            SET @name_of_table = CONCAT(database_name, counter);
            SET @create_tables = CONCAT('CREATE TABLE IF NOT EXISTS `',database_name,
                '`.`', @name_of_table, '` (id INT, name VARCHAR(255), surname VARCHAR(255), age INT);');
            PREPARE generate_tables FROM @create_tables;
            EXECUTE generate_tables;
            DEALLOCATE PREPARE generate_tables;
            SET counter = counter + 1;
        END WHILE;
    END LOOP;

    CLOSE main_cursor;
END //
DELIMITER ;

# Кінець процедури

# Збережені процедури другого пункту

DROP PROCEDURE IF EXISTS insert_rows;
DELIMITER //
CREATE PROCEDURE insert_rows()
BEGIN
    DECLARE counter INT DEFAULT 1;
    WHILE counter <= 10 DO
        INSERT INTO registration_confirmation (send_date, status,
          confirmation_code, expiration_date, User_id)
        VALUES (CURDATE(), 'pending', CONCAT('Noname',counter),
          DATE_ADD(CURDATE() ,INTERVAL 7 day), counter);
        SET counter = counter + 1;
    END WHILE;

END //
DELIMITER ;

DROP PROCEDURE IF EXISTS insert_into_hotel_location;
DELIMITER //
CREATE PROCEDURE insert_into_hotel_location(
     IN country VARCHAR(50),
     IN city VARCHAR(50),
     IN street VARCHAR(50),
     IN postal_code VARCHAR(20),
     IN Hotel_id INT
)
BEGIN
    INSERT INTO hotel_location (country, city, street, postal_code, Hotel_id)
      VALUES (country, city, street, postal_code, Hotel_id);

END //
DELIMITER ;

# кінець збережених процедур другого пункту