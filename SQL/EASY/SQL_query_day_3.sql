Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
ans :SELECT DISTINCT CITY FROM STATION WHERE NOT SUBSTR(city,1,1) IN ('A','E','I','O','U')
OR NOT SUBSTR(city,-1) IN ('a','e','i','o','u');

Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
ans : SELECT DISTINCT CITY FROM STATION WHERE NOT SUBSTR(city,1,1) IN ('A','E','I','O','U')
and NOT SUBSTR(city,-1) IN ('a','e','i','o','u');
