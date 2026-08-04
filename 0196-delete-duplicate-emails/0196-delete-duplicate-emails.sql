# Write your MySQL query statement below
DELETE p from Person p
join Person p2
Where p.id > p2.id and
p.email = p2.email;