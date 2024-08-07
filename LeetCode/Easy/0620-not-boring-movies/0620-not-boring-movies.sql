# Write your MySQL query statement below

SELECT
    id
    ,movie
    ,description
    ,rating
FROM Cinema
WHERE id % 2 = 1
AND description != 'boring'
order by 4 desc