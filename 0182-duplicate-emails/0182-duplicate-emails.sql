# Write your MySQL query statement below
SELECT email AS Email
FROM Person P
GROUP BY email
HAVING count(email) > 1;