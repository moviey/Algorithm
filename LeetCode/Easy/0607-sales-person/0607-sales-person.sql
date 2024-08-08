

# Write your MySQL query statement below
WITH namelist AS (SELECT
    name
FROM SalesPerson
WHERE sales_id in (SELECT
                        sales_id
                    FROM Orders
                    WHERE com_id in (SELECT
                                        com_id
                                    FROM Company
                                    WHERE name like 'red%')))

SELECT
    name
FROM SalesPerson
WHERE name not in (table namelist)