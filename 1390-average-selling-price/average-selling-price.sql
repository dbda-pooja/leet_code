# Write your MySQL query statement below
select p.product_id ,IFNULL(round(sum(u.units * p.price)/sum(u.units),2),0) as average_price
from prices p left join UnitsSold u 
ON p.product_id = u.product_id AND  p.start_date <= u.purchase_date and p.end_date >= u.purchase_date 
group by (product_id);

