-- # Write your MySQL query statement below
-- SELECT employee_id from Employees
-- where salary < 30000 and manager_id is in employee_id;

-- SELECT e.employee_id FROM Employees e
-- WHERE EXISTS (
--     SELECT employee_id FROM Employees m WHERE e.employee_id = m.manager_id and e.salary < 30000
-- );   

--  Approach 1 -- Left Join

-- SELECT e.employee_id from Employees e
-- left join Employees m 
-- On m.employee_id = e.manager_id
-- where e.salary < 30000 and m.employee_id is NULL
-- order by employee_id;

--  Approach 2 -- Subquery (NOT IN)

SELECT employee_id from Employees
Where salary < 30000 and manager_id NOT IN (select employee_id from Employees)
order by employee_id;