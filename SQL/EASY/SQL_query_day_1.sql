-- Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.
ans : SELECT  * from CITY where COUNTRYCODE = "USA" and Population>100000

--  Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
ans : SELECT CITY FROM STATION WHERE CITY REGEXP '^[AEIOU]'