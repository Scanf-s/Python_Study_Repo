use challenge;
create table customers(
	customer_id int primary key auto_increment,
	first_name varchar(25),
    last_name varchar(25),
    address varchar(100),
    city_name varchar(50)
);

create table products(
	product_id int primary key auto_increment,
	product_name varchar(25),
    price int,
    productline varchar(25) -- foreign key 설정해야함
);

create table employees(
	first_name varchar(25),
    last_name varchar(25),
    emp_rank varchar(10)
);

create table offices(
	city varchar(25),
    phone_number varchar(15)
);

create table orders(
	order_id int primary key auto_increment,
	order_date date,
    customer_id int, -- foreign key 설정해야함
    product_id int -- foreign key 설정해야함
);

create table orderdetails(
	order_id int, -- foreign key 설정해야함
    product_id int, -- foreign key 설정해야함
    quantityOrdered int,
    priceEach decimal(5, 2)
);

create table payments(
	customer_id int, -- foreign key 설정해야함
    amount decimal(5, 2),
    payment_date date
);

create table productlines(
	productline varchar(20),
    textdescription text
);

