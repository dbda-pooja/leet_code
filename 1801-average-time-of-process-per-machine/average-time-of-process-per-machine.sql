# Write your MySQL query statement below
select a.machine_id, round(avg(av.timestamp-a.timestamp),3) as processing_time
from Activity a cross join Activity av on a.machine_id = av.machine_id
where av.activity_type ='end' and a.activity_type ='start'
group by a.machine_id;
