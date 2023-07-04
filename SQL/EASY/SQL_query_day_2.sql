
-- Query all columns (attributes) for every row in the CITY table.
ans - select * from CITY

-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
ans - SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[AEIOU]'

-- Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
and - SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[AEIOU]' and CITY REGEXP '[AEIOU]$'

--Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
ans - Select distinct CITY from STATION where not CITY REGEXP '^[AEIOU]'

-- Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
ans - Select distinct CITY from STATION where not CITY REGEXP '[AEIOU]$'