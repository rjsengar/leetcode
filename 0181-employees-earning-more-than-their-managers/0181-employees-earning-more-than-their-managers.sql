# Write your MySQL query statement below
Select emp1.name AS Employee 
FROM Employee AS emp1
JOIN Employee AS emp2
ON emp1.managerID=emp2.id
WHERE emp1.salary>emp2.salary

