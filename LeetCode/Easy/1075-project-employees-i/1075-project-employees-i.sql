# Write your MySQL query statement below
SELECT
    project_id,
    round(sum(experience_years)/count(project_id),2) average_years 
FROM Project P
INNER JOIN Employee E
WHERE P.employee_id = E.employee_id
GROUP BY project_id