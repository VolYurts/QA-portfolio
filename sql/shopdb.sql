Create Database Shopdb;
use Shopdb;


CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2)
);


CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(50)
);


CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    employee_id INT,
    quantity INT,
    sale_date DATE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);


INSERT INTO Products (product_id, name, category, price)
VALUES
(1, 'Nokia 6230', 'Smartphones', 800.50),
(2, 'Xiaomi Redmi Note 13', 'Smartphones', 299.99),
(3, 'Apple Watch Series 9', 'Wearables', 250.99),
(4, 'iPhone 15 ProMax', 'Smartphones', 500.00),
(5, 'Sony WH-5000', 'Headphones', 200.99),
(6, 'Samsung Galaxy 2250', 'Smartphones', 230.99);



INSERT INTO Employees (employee_id, name, role)
VALUES
(1, 'Andrii Dziuba', 'Sales Manager'),
(2, 'Natali Melnyk', 'Sales Manager'),
(3, 'Oleg Stakh', 'Security'),
(4, 'Taras Koval', 'Courier'),
(5, 'Olena Denysenko', 'Store Director');


INSERT INTO Sales (sale_id, product_id, employee_id, quantity, sale_date) 
VALUES
(1, 1, 1, 2, '2025-06-01'),
(2, 2, 2, 1, '2025-06-02'),
(3, 3, 1, 3, '2025-06-03'),
(4, 4, 4, 1, '2025-06-03'),
(5, 1, 2, 1, '2025-06-04'),
(6, 5, 1, 4, '2025-06-05'),
(7, 6, 2, 2, '2025-06-05');


SELECT * FROM Products;

SELECT * FROM Employees;

SELECT * FROM Sales;

SELECT * FROM Products
WHERE name LIKE '%Sony%';

SELECT * FROM Products
WHERE category = 'Headphones';

SELECT * FROM Products
WHERE name LIKE 'i%e%';

SELECT * FROM Products
ORDER BY price DESC;

SELECT * FROM Products
ORDER BY price ASC;

SELECT * FROM Products
WHERE price BETWEEN 300 AND 600

SELECT AVG(price) AS average_price
FROM Products;

SELECT product_id, SUM(quantity) AS total_quantity_sold
FROM Sales
GROUP BY product_id;

SELECT product_id, COUNT(*) AS total_sales
FROM Sales
GROUP BY product_id;

SELECT name, price FROM Products
WHERE price = (SELECT MAX(price) FROM Products);

SELECT name, price FROM Products
WHERE price = (SELECT MIN(price) FROM Products);

SELECT * FROM Employees
WHERE role IN ('Sales Manager', 'Courier');

SELECT product_id, SUM(quantity) AS total_quantity_sold
FROM Sales
GROUP BY product_id
HAVING SUM(quantity) > 2;

SELECT * FROM Sales
WHERE sale_date >= '2025-06-05';

SELECT s.sale_id, s.product_id, p.name AS product_name
FROM Sales s
LEFT JOIN Products p ON s.product_id = p.product_id;

SELECT p.product_id, p.name, s.sale_id
FROM Products p
RIGHT JOIN Sales s ON s.product_id = p.product_id;

SELECT s.sale_id, p.name AS product_name, e.name AS employee_name, s.quantity, s.sale_date
FROM Sales s
JOIN Products p ON s.product_id = p.product_id
JOIN Employees e ON s.employee_id = e.employee_id;

SELECT s.sale_id, p.name AS product_name, e.name AS employee_name, s.quantity, s.sale_date
FROM Sales s
INNER JOIN Products p ON s.product_id = p.product_id
INNER JOIN Employees e ON s.employee_id = e.employee_id;

SELECT * FROM Products
Limit 3;

SELECT * FROM Products
LIMIT 2 OFFSET 3;


UPDATE Products
SET price = 135.50
WHERE product_id = 2;

UPDATE Products
SET price = 888.88
WHERE product_id IN (1,3,5)

UPDATE Products 
SET price = price + 150
WHERE name LIKE '%o%';


UPDATE Products
SET price = price * 0.5
WHERE category = 'Smartphones';

SELECT product_id, name, price FROM Products WHERE product_id = 6;

UPDATE Products
SET price = ROUND(price * 0.5, 2)
WHERE category = 'Smartphones';

SELECT SUM(quantity) AS total_items_sold
FROM Sales;

DELETE FROM Products
WHERE name = 'Nokia 6230';

DELETE FROM Products;

DROP TABLE Products;

DROP DATABASE shopdb;









