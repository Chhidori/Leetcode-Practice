# Write your MySQL query statement below
Select max(salary) as 'SecondHighestSalary'
    From Employee
    Where salary < (SELECT max(salary) From Employee)