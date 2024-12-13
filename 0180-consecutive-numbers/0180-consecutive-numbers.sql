# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums
FROM(SELECT *,LEAD(num) OVER() AS Nexta,LEAD(num,2) OVER() AS Nextb
FROM Logs) AS nums
WHERE nums.num=nums.Nexta AND nums.Nexta=nums.Nextb