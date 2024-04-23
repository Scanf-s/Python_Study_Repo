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
-- 1. employees 테이블에서 여러 직원의 부서를 한 번에 갱신하세요.
update employees
set officeCode = 9
where employeeNumber >= 2000

-- 2. offices 테이블에서 여러 사무실의 위치를 한 번에 갱신하세요.
update offices
set addressLine1 = "new address"
where country = "Korea";

-- 3. orders 테이블에서 지난 달의 모든 주문의 배송 상태를 갱신하세요.
update orders
set status = "Shipped"
where orderDate BETWEEN '2024-03-01' and '2024-03-31'

-- 4. orderdetails 테이블에서 여러 주문 상세 가격을 한 번에 갱신하세요.
update orderdetails
set priceEach = 3.99
where quantityOrdered > 10 and productCode = "S99_0006";

-- 5. payments 테이블에서 특정 고객의 모든 지불 내역을 갱신하세요.
update payments
set amount = amount * 1.05
where customerNumber = 500

-- 6. productlines 테이블에서 여러 제품 라인의 설명을 한 번에 갱신하세요.
update productlines
set textDescription = "New description"
where productLine = "Temp"

-- 7. customers 테이블에서 특정 지역의 모든 고객의 연락처를 갱신하세요.
update customers
set phone = "010-2222-2222"
where country = "Korea"

-- 8. products 테이블에서 특정 카테고리의 모든 제품 가격을 갱신하세요
update products
set buyPrice = "999.00"
where productLine = "Ships"

-- 9. employees 테이블에서 특정 직원의 모든 정보를 갱신하세요.
update employees
set salary = "1234", email = "newemail@email.com"
where employeeNumber = "1234"

-- 10. offices 테이블에서 특정 사무실의 모든 정보를 갱신하세요.
update offices
set addressLine1 = "New addr1", addressLine2 = "New addr2", phone = "12345555"
where officeCode = "7"

-- 고급
-- 1. orders 테이블에서 지난 해의 모든 주문 상태를 갱신하세요.
update orders
set status = "Done"
where shippedDate BETWEEN '2023-01-01' and '2023-12-31';

-- 2. orderdetails 테이블에서 특정 주문의 모든 상세 정보를 갱신하세요.
update orderdetails
set quantityOrdered = 33, priceEach = 1.99
where orderNumber = 100000;

-- 3. payments 테이블에서 지난 달의 모든 지불 내역을 갱신하세요.
update payments
set paymentDate = curdate()
where paymentDate between '2024-03-01' and '2024-03-31'

-- 4. productlines 테이블에서 모든 제품 라인의 정보를 갱신하세요.
update productlines
set htmlDescription = "<h1>YAY</h1>"

-- 5. customers 테이블에서 모든 고객의 주소를 갱신하세요.
update customers
set addressLine1 = "New address!!!"

