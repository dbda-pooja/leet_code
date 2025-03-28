# Write your MySQL query statement below
select e.employee_id ,e.name , count(*) as reports_count,round(avg(e1.age),0) as average_age
from Employees e join employees e1
on (e.employee_id)=(e1.reports_to)
group by e.employee_id
order by employee_id asc;