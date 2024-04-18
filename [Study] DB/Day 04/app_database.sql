SET SQL_SAFE_UPDATES = 0;

create database testdatabase;
use testdatabase;
drop table users;
create table users(
	user_id int primary key auto_increment,
	username varchar(50),
    email varchar(50)
);

create table orders(
    user_id int,
    product_name varchar(50),
    quantity int
);

select * from users;
select * from orders;