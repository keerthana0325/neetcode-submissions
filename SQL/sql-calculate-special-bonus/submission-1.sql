-- Write your query below
-- select employee_Id, 
-- CASE when
-- employee_id%2!=0 and NOT like 'M%' then
-- salary = 100%*salary
-- else
-- salary = 0
-- AS bonus 
-- -smy
SELECT
    employee_id,
    CASE
        WHEN employee_id % 2 != 0
             AND name NOT LIKE 'M%'
        THEN salary
        ELSE 0
    END AS bonus
FROM Employees order by employee_id;