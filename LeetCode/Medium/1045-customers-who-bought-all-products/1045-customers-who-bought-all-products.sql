# Write your MySQL query statement below
WITH CNT AS (SELECT
        customer_id,
        COUNT(DISTINCT product_key) cnt
        FROM Customer 
        GROUP BY customer_id)

SELECT
    customer_id 
FROM CNT 
WHERE cnt = (
                SELECT
                    COUNT(DISTINCT product_key) cnt
                FROM Product
)