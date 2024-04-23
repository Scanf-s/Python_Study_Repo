-- 초급
-- 1. customers 테이블에서 특정 고객을 삭제하세요.
select * from customers;
delete from customers
where customerNumber = 501;

-- 2. products 테이블에서 특정 제품을 삭제하세요.
select * from products;
delete from products
where productCode = "S99_0003"

-- 3. employees 테이블에서 특정 직원을 삭제하세요.
select * from employees;
delete
from employees
where employeeNumber = 2002;

-- 4. offices 테이블에서 특정 사무실을 삭제하세요.
select * from offices;
delete
from offices
where city="Seoul";

-- 5. orders 테이블에서 특정 주문을 삭제하세요.
select * from orders;
delete
from orderdetails
where orderNumber = 100000;

-- 6. orderdetails 테이블에서 특정 주문 상세를 삭제하세요.
select * from orderdetails where orderNumber >= 99999;
delete
from orderdetails
where orderNumber = 10000;

-- 7. payments 테이블에서 특정 지불 내역을 삭제하세요.
select * from payments;
delete
from payments
where customerNumber = 499;

-- 8. productlines 테이블에서 특정 제품 라인을 삭제하세요.
select * from productlines;
delete
from productlines
where productLine = "Temp2";

-- 9. customers 테이블에서 특정 지역의 모든 고객을 삭제하세요.
select * from customers;
delete
from customers
where city like "ak% City";

-- 10. products 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
select * from products;
delete
from products
where productLine = "Temp2";

-- 중급
-- 1.