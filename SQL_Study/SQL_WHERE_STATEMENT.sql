-- Selecting Data that Satisfies Specified Conditions
Selecting Data for some specific Condition
ans : select {column_1},{column_2} from {table_name} where {Condition_1}=true

-- Here I use HR Data for practics SQL queries. 
Selecting Data for Last Names that Start with the Same Substring
ans : select FIRST_NAME , LAST_NAME from employees where LAST_NAME LIKE 'Ma%';

Selecting Data that Satisfies Two Conditions
ans :SELECT FIRST_NAME ,LAST_NAME FROM employees WHERE (SALARY>=9000) AND (COMMISSION_PCT IS NOT NULL);
