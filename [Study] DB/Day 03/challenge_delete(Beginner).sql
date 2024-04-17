-- 1. customers 테이블에서 특정 고객을 삭제하세요
select * from customers;

delete from customers
where customer_id = 100;

select * from customers;

-- 2. products 테이블에서 특정 제품을 삭제하세요.
select * from products;
insert into products(product_name, price, productline)
values ("MapleStory", 0, "Game");
select * from products;

delete from products
where product_name = "MapleStory";

select * from products;

-- 3. employees 테이블에서 특정 직원을 삭제하세요
select * from employees;
insert into employees(first_name, last_name, emp_rank)
values ("UIJONG", "YANG", "CEO");
select * from employees;

delete from employees
where first_name = "UIJONG";

select * from employees;

-- 4. offices 테이블에서 특정 사무실을 삭제하세요.alter
insert into offices (city, phone_number)
values ("Jeju", "064-1111-1111");

select * from offices;

delete from offices
where phone_number = "064-1111-1111";

select * from offices;

-- 5. orders 테이블에서 특정 주문을 삭제하세요
select * from orders;
insert into orders(order_date, customer_id, product_id)
values(now(), 101, 2);
select * from orders;

delete from orders
where customer_id = 1;

select * from orders;

-- 6. orderdetails 테이블에서 특정 주문 상세를 삭제하세요.
select * from orderdetails;
insert into orderdetails(order_id, product_id, quantityOrdered, priceEach)
values (1001, 2, 5, 100.00);
select * from orderdetails;

delete from orderdetails
where order_id = 1001;
select * from orderdetails;

-- 7. payments 테이블에서 특정 지불 내역을 삭제하세요.
select * from payments;
delete from payments
where customer_id = 100;
select * from payments;

-- 8. productlines 테이블에서 특정 제품 라인을 삭제하세요.
select * from productlines;
insert into productlines(productline, textdescription)
values("Gun", "ammo guns");
select * from productlines;

delete from productlines
where productline = "Gun";
select * from productlines;

-- 9. customers 테이블에서 특정 지역의 모든 고개을 삭제하세요.
select * from customers;

alter table customers
alter email set default "not yet submitted";

insert into customers(first_name, address, city_name)
values 
	("Fenix", "Khalai", "Protoss"),
	("Tassadar", "Khalai", "Protoss");
select * from customers;

delete from customers
where city_name = "Protoss";
select * from customers;

-- 10. products 테이블에서 특정 카테고리의 모든 제품을 삭제하세요
select * from products;
insert into products(product_name, price, productline)
values 
	("AK47", "300.00", "Gun"),
	("K2", "0.00", "Gun"),
    ("M4A1", "700.00", "Gun");
    
select * from products;

delete from products
where price >= 300;
select * from products;
    


