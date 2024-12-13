# Write your MySQL query statement below
SELECT email AS Email
From Person
GROUP BY email
HAVING COUNT(DISTINCT id)>1