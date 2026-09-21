# Write your MySQL query statement below
select product_name,year,price 
from product 
left join sales
on sales.product_id=product.product_id
where year is not null;