# Write your MySQL query statement below

SELECT
    activity_date day        
    ,COUNT(DISTINCT user_id) active_users 
FROM Activity 
WHERE activity_date BETWEEN DATE_SUB('2019-07-27', INTERVAL 30 DAY)+1 AND '2019-07-27'
GROUP BY activity_date
