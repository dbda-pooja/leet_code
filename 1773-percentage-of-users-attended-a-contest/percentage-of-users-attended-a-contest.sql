# Write your MySQL query statement below
select r.contest_id,round((count(r.user_id)/(select count(user_id) from users))*100,2) as percentage
from Users u , Register r
where u.user_id = r.user_id
group by r.contest_id
order by 2 desc ,1 asc
;