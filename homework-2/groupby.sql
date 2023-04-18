-- Напишите запросы, которые выводят следующую информацию:
-- 1. заказы, отправленные в города, заканчивающиеся на 'burg'. Вывести без повторений две колонки (город, страна) (см. таблица orders, колонки ship_city, ship_country)
SELECT DISTINCT ship_city AS city, ship_country AS country FROM orders
WHERE ship_city LIKE '%burg';

-- 2. из таблицы orders идентификатор заказа, идентификатор заказчика, вес и страну отгрузки. Заказ отгружен в страны, начинающиеся на 'P'. Результат отсортирован по весу (по убыванию). Вывести первые 10 записей.
SELECT DISTINCT order_id, customer_id, freight, ship_country FROM orders 
WHERE ship_country LIKE 'P%'
ORDER BY freight DESC LIMIT 10

-- 3. фамилию и телефон сотрудников, у которых в данных отсутствует регион (см таблицу employees)
SELECT last_name, home_phone  FROM employees
WHERE region IS null;

-- 4. количество поставщиков (suppliers) в каждой из стран. Результат отсортировать по убыванию количества поставщиков в стране
SELECT country, COUNT(company_name) AS count_company FROM suppliers
GROUP BY country
ORDER BY count_company DESC;

-- 5. суммарный вес заказов (в которых известен регион) по странам, но вывести только те результаты, где суммарный вес на страну больше 2750. Отсортировать по убыванию суммарного веса (см таблицу orders, колонки ship_region, ship_country, freight)
SELECT ship_country, SUM(freight) AS weight FROM orders
WHERE ship_region != 'null'
GROUP BY ship_country
HAVING SUM(freight) > 2750
ORDER BY weight DESC

-- 6. страны, в которых зарегистрированы и заказчики (customers) и поставщики (suppliers) и работники (employees).
SELECT DISTINCT country FROM customers
UNION
SELECT DISTINCT country FROM suppliers
UNION
SELECT DISTINCT country FROM employees;

-- 7. страны, в которых зарегистрированы и заказчики (customers) и поставщики (suppliers), но не зарегистрированы работники (employees).
SELECT DISTINCT country FROM customers
UNION ALL
SELECT DISTINCT country FROM suppliers
EXCEPT
SELECT DISTINCT country FROM employees;
