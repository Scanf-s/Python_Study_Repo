-- 1. customers 테이블에 새 고객을 추가하세요.
insert into customers (first_name, last_name, address, city_name)
values("UIJONG", "YANG", "asdf st.", "Seoul");
select * from customers;

-- 2. products 테이블에 새 제품을 추가하세요
insert into products (product_name, price, productline)
values("GTA5", 35.00, "Game");
select * from products;

-- 3. employees 테이블에 새 직원을 추가하세요
insert into employees (first_name, last_name, emp_rank)
values("SEONGTAE", "KIM", "CEO");
select * from employees;

-- 4. offices 테이블에 새 사무실을 추가하세요
insert into offices (city, phone_number)
values("Seoul", "02-1234-1234");
select * from offices;

-- 5. orders 테이블에 새 주문을 추가하세요
alter table orders
modify column order_date datetime;

insert into orders (order_date, customer_id, product_id)
values(now(), 1, 1);
select * from orders;

-- 6. orderdetails 테이블에 주문 상세 정보를 추가하세요
insert into orderdetails (order_id, product_id, quantityOrdered, priceEach)
values(1000, 1, 5, 35.00);
select * from orderdetails;

-- 7.payments테이블에 지불 정보를 추가하세요.
alter table payments
modify column payment_date datetime;
insert into payments (customer_id, amount, payment_date)
values(100, 5, now());
select * from payments;

delete from payments;
-- 8.productlines 테이블에 제품 라인을 추가하세요.

insert into productlines (productline, textdescription)
values ("Game", "online, video games");
select * from productlines;

-- 9.customers 테이블에 다른 지역의 고객을 추가하세요.
insert into customers (first_name, last_name, address, city_name)
values("Raynor", "Jim", "fdsa st.", "Mar Sara");
select * from customers;

-- 10.products 테이블에 다른 카테고리의 제품을 추가하세요.
insert into products (product_name, price, productline)
values("Gauss Rifle", 899.91, "Gun");
select * from products;