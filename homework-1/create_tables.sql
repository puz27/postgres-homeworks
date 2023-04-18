CREATE TABLE customers (
	customer_id VARCHAR(20) PRIMARY KEY, 
	company_name VARCHAR(50) NOT NULL, 
	contact_name VARCHAR(30));


CREATE TABLE orders (
	order_id INT PRIMARY KEY, 
	customer_id VARCHAR(30) REFERENCES CUSTOMERS(customer_id) not NULL , 
	employee_id INT NOT NULL, 
	order_date DATE NOT NULL, 
	ship_city VARCHAR(30) NOT NULL);
	
	
CREATE TABLE employees (
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	title VARCHAR(50) NOT NULL,
	birth_date DATE NOT NULL,
	notes TEXT);