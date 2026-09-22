# Write your MySQL query statement below
select e.machine_id ,round(avg(s.timestamp-e.timestamp),3) 
as processing_time
from activity s join activity e on
s.machine_id=e.machine_id and s.process_id =e.process_id and
e.activity_type='start' and s.activity_type='end'
group by e.machine_id;
