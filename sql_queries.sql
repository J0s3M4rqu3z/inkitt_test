#how much did they read? if we uderstand the quantyty as number of entrancies per day 
SELECT visitor_id,count(reading.visitor_id) quantity_by_day,date(created_at) as reading_day
FROM reading
left join stories on reading.story_id = stories.id 
where concat(category_one,' ',category_two) regexp 'horror'
group by visitor_id,date(created_at);

#how much did they read? if we uderstand the quantyty as seconds that the visitor was in ur plataform in total
#but for the data kind i think is the first one
SELECT visitor_id,sum(timestampdiff(second,tracking_time,created_at)) as quantity_by_day,date(created_at) as reading_day
FROM reading
left join stories on reading.story_id = stories.id 
where concat(category_one,' ',category_two) regexp 'horror'
group by visitor_id,date(created_at);

#how many readers are there?

SELECT count(distinct reading.visitor_id) quantity_by_day,date(created_at) as reading_day
FROM reading
left join stories on reading.story_id = stories.id 
left join visits on visits.visitor_id = reading.visitor_id
where concat(category_one,' ',category_two) regexp 'horror'
group by date(created_at);

#what country are the readers from? Understading that we want to know from where the readers are on one day
SELECT country, date(created_at) as read_day
FROM reading
left join stories on reading.story_id = stories.id 
left join visits on visits.visitor_id = reading.visitor_id
where concat(category_one,' ',category_two) regexp 'horror'
group by date(created_at),country;
