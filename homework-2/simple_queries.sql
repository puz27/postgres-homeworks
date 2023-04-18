-- Напишите запросы, которые выводят следующую информацию:
-- 1. "имя контакта" и "город" (contact_name, country) из таблицы customers (только эти две колонки)
select contact_name, country from customers;

-- 2. идентификатор заказа и разницу между датами формирования (order_date) заказа и его отгрузкой (shipped_date) из таблицы orders
select order_id, ABS(order_date - shipped_date) AS Forming  from orders;

-- 3. все города без повторов, в которых зарегистрированы заказчики (customers)
select DISTINCT city from customers;

-- 4. количество заказов (таблица orders)
select COUNT(order_id) AS count_all_orders from orders;

-- 5. количество стран, в которые отгружался товар (таблица orders, колонка ship_country)
select COUNT(DISTINCT ship_country) AS count_all_countrys from orders;
