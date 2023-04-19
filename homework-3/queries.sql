-- Напишите запросы, которые выводят следующую информацию:
-- 1. Название компании заказчика (company_name из табл. customers) и ФИО сотрудника, работающего над заказом этой компании (см таблицу employees),
-- когда и заказчик и сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United Package (company_name в табл shippers)
    SELECT customers.company_name, CONCAT(employees.first_name ,employees.last_name) AS fio FROM orders
    INNER JOIN customers
    ON orders.customer_id = customers.customer_id AND customers.city = 'London'
    INNER JOIN employees
    ON orders.employee_id = employees.employee_id AND employees.city = 'London'
    INNER JOIN shippers
    ON orders.ship_via = shippers.shipper_id AND shippers.company_name = 'United Package'

-- 2. Наименование продукта, количество товара (product_name и units_in_stock в табл products),
-- имя поставщика и его телефон (contact_name и phone в табл suppliers) для таких продуктов,
-- которые не сняты с продажи (поле discontinued) и которых меньше 25 и которые в категориях Dairy Products и Condiments.
-- Отсортировать результат по возрастанию количества оставшегося товара.
    SELECT products.product_name, products.units_in_stock, suppliers.contact_name ,suppliers.phone FROM products
    INNER JOIN suppliers
    ON products.supplier_id = suppliers.supplier_id AND discontinued = 0 AND units_in_stock < 25
    INNER JOIN categories
    ON products.category_id = categories.category_id AND category_name IN ('Dairy Products','Condiments')
    ORDER BY units_in_stock

-- 3. Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа
    SELECT customers.company_name FROM customers
    LEFT JOIN orders
    ON customers.customer_id = orders.customer_id 
    WHERE orders.customer_id IS NULL

-- 4. уникальные названия продуктов, которых заказано ровно 10 единиц (количество заказанных единиц см в колонке quantity табл order_details)
-- Этот запрос написать именно с использованием подзапроса.
    SELECT DISTINCT order_details.product_id,order_details.quantity , products.product_id, products.product_name FROM order_details
    INNER JOIN products
    ON order_details.product_id = products.product_id 
    WHERE order_details.quantity = 10
    ORDER BY product_name
