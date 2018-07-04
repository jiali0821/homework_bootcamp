1a. 
SELECT first_name, last_name
FROM actor;

1b. 
SELECT UPPER(CONCAT(first_name, ' ', last_name)) AS Actor_Name
FROM actor;

2a.
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = "Joe";


2b.
SELECT *
FROM actor
WHERE last_name LIKE '%GEN%';

2c.
SELECT *
FROM actor
WHERE last_name LIKE '%LI%'
ORDER BY last_name, first_name; 


2d.
SELECT country_id, country
FROM country
WHERE country in ('Afghanistan', 'Bangladesh', 'China')


3a.
ALTER TABLE actor
ADD COLUMN middle_name varchar(25) AFTER last_name;


3b.

3c.
ALTER TABLE actor
DROP COLUMN middle_name;


 