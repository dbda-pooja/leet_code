# Write your MySQL query statement below
select date_format(t.trans_date , '%Y-%m') as month, t.country , count(*) as trans_count,
count(case when t.state = 'approved'  THEN 1 END) as approved_count,
sum(t.amount) as trans_total_amount,
sum(case when t.state = 'approved' then t.amount else 0 end) as approved_total_amount
from Transactions  t
group by date_format(t.trans_date , '%Y-%m'),t.country  ;