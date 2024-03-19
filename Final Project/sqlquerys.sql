SELECT river.id, city.name as city_name, start_coord, end_coord, river_length, highest_rappel, croqui
FROM river
JOIN city ON river.city_id = city.id;

SELECT river.id, city.name as city_name, river.name as river_name, start_coord, end_coord, river_length, highest_rappel, croqui
FROM river
JOIN city ON river.city_id = city.id;

SELECT city.name as city_name, river.name as river_name, start_coord, end_coord, river_length, highest_rappel, croqui
FROM river
JOIN city ON river.city_id = city.id;

UPDATE river
SET city_id = 2
WHERE name =  'Arador Inferior';

SELECT city.name as city_name, river.name as river_name, start_coord, end_coord, river_length, highest_rappel, croqui FROM river
JOIN city ON river.city_id = city.id
WHERE city.name = 'Braga';
