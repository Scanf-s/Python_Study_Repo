-- 1. customers 테이블에서 특정 고객의 주소를 갱신하세요
update customers
set address = "dokdo kick"
where first_name = "UIJONG";

select * from customers where first_name = "UIJONG";

-- 2. products 테이블에서 특정 제품의 가격을 갱신하세요.
update products
set price = 15.00
where product_name = "GTA5";

select * from products where product_name = "GTA5";

-- 3. employees 테이블에서 특정 직원의 직급을 갱신하세요.
update employees
set emp_rank = "Staff"
where first_name = "SEONGTAE";

select * from employees;

-- 4. offices 테이블에서 특정 사무실의 전화번호를 갱신하세요.
update offices
set phone_number = "02-1111-1111"
where city = "Seoul";

select * from offices;

-- 5. orders 테이블에서 특정 주문의 상태를 갱신하세요.
update orders
set product_id = 2
where order_id = 1000;

select * from orders;

-- 6. orderdetails 테이블에서 특정 주문 상세의 수량을 갱신하세요alter
update orderdetails
set quantityOrdered = 100
where product_id = 1;

select * from orderdetails;

-- 7. payments 테이블에서 특정 지불 금액을 갱신하세요.
select * from payments;
update payments
set amount = 900.00
where customer_id = 100;

select * from payments;

-- 8. productlines 테이블에서 특정 제품 라인의 설명을 갱신하세요.
update productlines
set textdescription = "famous game"
where productline = "Game";

select * from productlines;

-- 9. customers 테이블에서 특정 고객의 이메일을 갱신하세요.
alter table customers
add email varchar(50);

update customers
set email = "not yet submitted"
where email is NULL;

select * from customers;

-- 10. products 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
update products
set price = 100.00; -- 상품이 2개밖에 없어서 그냥 전체 적용했습니다.

select * from products;