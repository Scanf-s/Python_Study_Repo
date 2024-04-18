-- 초급
-- 1. customers 테이블에서 특정 고객의 주소를 갱신하세요
update customers
set addressLine1 = "Modified..."
where customerName = "Scanf-s";
select * from customers where customerName = "Scanf-s";

-- 2. products 테이블에서 특정 제품의 가격을 갱신하세요
select * from products;
update products
set buyPrice = 123.32
where productCode = "S99_0000";
select * from products where productCode = "S99_0000";

-- 3. employees 테이블에서 특정 직원의 직급을 갱신하세요.
select * from employees;
update employees
set jobTitle = "Sales Rep"
where employeeNumber = 2004;

-- 4. offices 테이블에서 특정 사무실의 전화번호를 갱신하세요.
select * from offices;
update offices
set phone = "+82 10 0000 1234"
where officeCode = 8;

-- 5. orders 테이블에서 특정 주문의 상태를 갱신하세요.
select * from orders;
update orders
set shippedDate = curdate(), status = "Shipped"
where orderNumber = 99999;

-- 6. orderdetails 테이블에서 특정 주문 상세의 수량을 갱신하세요.
select * from orderdetails where orderNumber >= 99999;
update orderdetails
set quantityOrdered = 50
where orderNumber = 99999;

-- 7. payments 테이블에서 특정 지불의 금액을 갱신하세요
select * from payments;
update payments
set amount = 50000.00
where customerNumber = 497;

-- 8. productlines 테이블에서 특정 제품 라인의 설명을 갱신하세요
select * from productlines;
update productlines
set textDescription = "Modified description"
where productLine = "Temp";

-- 9. employees 테이블에서 특정 직원의 이메일을 갱신하세요.
select * from employees;
update employees
set email = "modified_email@test.com"
where employeeNumber = 2000;

-- 10. products 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
select * from products;
update products
set buyPrice = 5555.55
where productCode like "S9%";

-- 중급
-- 1.