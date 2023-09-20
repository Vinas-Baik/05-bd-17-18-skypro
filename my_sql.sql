-- В данном запросе происходит объединение результатов двух запросов:
-- первый запрос выбирает данные из таблицы customers,
-- а второй запрос — данные из таблицы suppliers.
-- Оба запроса выбирают данные из столбца country.
-- UNION объединяет результаты этих двух запросов и выдает единый результат,
-- который содержит уникальные строки из обеих таблиц.

SELECT country FROM customers
UNION
SELECT country FROM suppliers

-- запрос вернет только те страны, которые есть и в первом, и во втором запросе:
-- INTERSECT — оператор, который используется для получения пересечения результатов
-- двух или более запросов. Он возвращает только те строки, которые присутствуют
-- в обоих запросах. Результаты должны иметь одинаковое число столбцов, и
-- соответствующие столбцы должны иметь совместимые типы данных.

SELECT country FROM customers
INTERSECT
SELECT country FROM suppliers

-- запрос вернет из таблицы orders страны (колонка ship_country) и количество заказов в каждой стране.
-- Результаты будут отсортированы в порядке убывания количества заказов

SELECT ship_country, COUNT(*)
FROM orders
GROUP BY ship_country
ORDER BY COUNT(*) DESC;

-- В данном запросе происходит группировка заказов по странам, а затем вычисляется
-- количество заказов в каждой стране. Однако результаты будут показаны только
-- для тех стран, в которых количество заказов больше 30:

SELECT ship_country, COUNT(*)
FROM orders
GROUP BY ship_country
HAVING COUNT(*) > 30
ORDER BY COUNT(*) DESC;

-- запрос вернет в порядке убывания количество заказов по регионам USA (где регион указан)
-- и ограничит выборку только теми записями, где количество таких заказов больше 10:

SELECT ship_region, ship_country, COUNT(*)
FROM orders
WHERE ship_region IS NOT NULL AND ship_country = 'USA'
GROUP BY ship_region, ship_country
HAVING COUNT(*) > 10
ORDER BY COUNT(*) DESC;



SELECT * FROM orders
WHERE EXISTS (SELECT * FROM employees
              WHERE orders.employee_id=employees.employee_id AND
                    orders.ship_country=employees.country)


SELECT * FROM orders
INNER JOIN employees
ON orders.employee_id=employees.employee_id and
   orders.ship_country=employees.country