-- 1. customers 테이블에서 모든 고객 정보를 조회하세요.
select * from customers;

-- 2. products 테이블에서 모든 제품 목록을 조회하세요.
select * from products;

-- 3. employees 테이블에서 모든 직원의 이름과 직급을 조회하세요.
select first_name, emp_rank from employees;

-- 4. offices 테이블에서 모든 사무실의 위치를 조회하세요.
select city from offices;

-- 5. orders 테이블에서 최근 10개의 주문을 조회하세요
select * from orders limit 10;

-- 6. orderdetails 테이블에서 특정 주문의 모든 상세정보를 조회하세요.
select * from orderdetails
where order_id = 1000;

-- 7. payments 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
select * from payments
where customer_id = 100;

-- 8. productlines 테이블에서 각 제품 라인의 설명을 조회하세요
select textdescription from productlines;

-- 9. customers 테이블에서 특정 지역의 고객을 조회하세요.
select * from customers
where city_name = "Seoul";

-- 10. products 테이블에서 특정 가격 범위의 제품을 조회하세요
select * from products
where price >= 550.00;
