/*
problem:
Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.
*/
Answer:
SELECT name from Employee order by name;


/*
problem:
Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having 
a salary greater than $2000 per month who have been employees for less than 10  months. Sort your result by ascending employee_id.
*/
Answer:
Select name from Employee  where months<10 and salary>2000;

/*
problem:
Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

Equilateral: It's a triangle with  sides of equal length.
Isosceles: It's a triangle with  sides of equal length.
Scalene: It's a triangle with  sides of differing lengths.
Not A Triangle: The given values of A, B, and C don't form a triangle.
*/
Answer:
Select case
        when A+B <= C OR A+C <= B OR B+C <= A then "Not A Triangle"
        when A = B AND B = C  then "Equilateral"
        when A = B OR B = C OR A = C then "Isosceles"
        else "Scalene"
    END 
    from TRIANGLES;

/*
Problem:
Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.
*/
Answer:
Select sum(CITY.POPULATION) from COUNTRY 
INNER JOIN CITY
 ON COUNTRY.CODE = CITY.COUNTRYCODE
where COUNTRY.CONTINENT = "Asia";
