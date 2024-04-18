create table employees(
	id int primary key auto_increment,
    name varchar(100),
    position varchar(100),
    salary decimal(10, 2)
);
select * from employees;

insert into employees (name, position, salary)
values 
	("헤린", "PM", 90000), 
	("은우", "Frontend", 80000), 
    ("가을", "Backend", 92000), 
    ("지수", "Frontend", 78000), 
    ("민혁", "Frontend", 96000), 
    ("하온", "Backend", 130000);

select name, salary from employees;

select name, salary from employees
where salary <= 90000;

update employees
set salary = salary * 1.1
where position = "PM";
select * from employees;

update employees
set salary = salary * 1.05
where position = "Backend";

delete from employees
where name = "민혁";

select position, avg(salary) as "Average Salary" from employees
group by position;

drop table employees;