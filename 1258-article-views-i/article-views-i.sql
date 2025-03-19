# Write your MySQL query statement below
select distinct viewer_id as id from Views v where v.viewer_id = v.author_id order by id 