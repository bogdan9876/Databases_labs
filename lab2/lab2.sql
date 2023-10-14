
-- 1. БД «Комп. фірма». Знайдіть номер моделі, швидкість та розмір
-- жорсткого диску для всіх ноутбуків, екран яких не менше 12 дюймів.
-- Вивести: model, speed, hd, price. Вихідні дані впорядкувати за спаданням за стовицем price.
SELECT model, speed, hd, price FROM laptop
WHERE screen <= 12
ORDER BY price DESC;

-- 2. БД «Фірма прий. вторсировини». З таблиці Outcome
-- вивести всю інформацію за березень місяць.
SELECT * FROM outcome
WHERE MONTH(date) = 3 ;

-- 3. БД «Комп. фірма». Знайдіть номер моделі та виробника ПК, яка має
-- ціну менше за 600 дол. Вивести: model, maker.
SELECT DISTINCT PC.model, Product.maker FROM PC
JOIN Product ON PC.model = Product.model
WHERE PC.price < 600;


-- 4. БД «Комп. фірма». Знайдіть виробників, що випускають одночасно
-- ПК та ноутбуки (використати ключове слово ALL). Вивести maker.
SELECT DISTINCT maker FROM Product P1 WHERE type = 'PC'
AND EXISTS (
    SELECT *
    FROM Product P2
    WHERE P2.type = 'Laptop'
    AND P1.maker = P2.maker
);

-- 5. БД «Комп. фірма». Виведіть тих виробників ноутбуків, які не
-- випускають принтери. Вивести maker.
SELECT DISTINCT maker FROM Product
WHERE type = 'Laptop'
AND maker NOT IN (
    SELECT maker
    FROM Product
    WHERE type = 'Printer'
);

-- 6. БД «Комп. фірма». Виведіть середню ціну ноутбуків із попереднім
-- текстом 'середня ціна ='
SELECT CONCAT('середня ціна = ', AVG(price)) AS average_price FROM laptop;

-- 7. БД «Комп. фірма». Знайдіть виробників найдешевших чорно-білих
-- принтерів. Вивести: maker, price.
SELECT Product.maker, MIN(Printer.price) AS price FROM Printer
INNER JOIN Product ON Printer.model = Product.model
WHERE Printer.color = 'n'
GROUP BY Product.maker;

-- 8. БД «Комп. фірма». Для таблиці Product отримати підсумковий набір
-- у вигляді таблиці зі стовпцями maker, pc, laptop a printer, у якій для
-- кожного виробника необхідно вказати кількість продукції, що ним
-- випускається, тобто наявну загальну кількість продукції в таблицях,
-- Відповідно , РС, Laptop тa Printer. (Підказка: використовувати підза-
-- пити в якості обчислювальних стовпців)
SELECT maker,
       COUNT(CASE WHEN type = 'PC' THEN 1 END) AS pc,
       COUNT(CASE WHEN type = 'Laptop' THEN 1 END) AS laptop,
       COUNT(CASE WHEN type = 'Printer' THEN 1 END) AS printer
FROM Product
GROUP BY maker;

-- 9. БД «Фірма прий. вторсировини». Приймаючи, що прихід та розхід
-- грошей на кожному пункті прийому може фіксуватися довільне число
-- раз на день (лише таблиці Income та Outcome), написати запит із таки-
-- ми вихідними даними: point (пункт), date (дата), іпс (прихід), out
-- (розхід), у якому в кожному пункті за кожну дату відповідає лише
-- одна стрічка. (Підказка: використовувати зовнішнє зʼєднання та
-- оператор CASE)
SELECT point, date, SUM(inc) AS inc, SUM(`out`) AS `out`
FROM ( SELECT point, date, SUM(inc) AS inc, 0 AS `out` 
		FROM Income_o
        GROUP BY point, date
        UNION ALL
        SELECT point, date, 0 AS inc, SUM(`out`) AS `out`
        FROM Outcome_o
        GROUP BY point, date ) AS combined
GROUP BY point, date
ORDER BY point, date;


-- 10. БД «Комп. фірма». Знайдіть номера моделей та ціни всіх продуктів
-- (будь-якого типу), що випущені виробником 'В'. Вивести: так,
-- model, type, price. (Підказка: використовувати оператор UNION)
SELECT PC.model, 'PC' AS type, PC.price FROM PC
INNER JOIN Product ON PC.model = Product.model
WHERE Product.maker = 'B'
UNION
SELECT Laptop.model, 'Laptop' AS type, Laptop.price FROM Laptop
INNER JOIN Product ON Laptop.model = Product.model
WHERE Product.maker = 'B'
UNION
SELECT Printer.model, 'Printer' AS type, Printer.price FROM Printer
INNER JOIN Product ON Printer.model = Product.model
WHERE Product.maker = 'B';
