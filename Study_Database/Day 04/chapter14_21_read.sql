-- 초급
-- 1. customers 테이블에서 모든 고객 정보를 조회하세요.
select * from customers;

-- 2. products 테이블에서 모든 제품 목록을 조회하세요.
select * from products;

-- 3. employees 테이블에서 모든 직원의 이름과 직급을 조회하세요
select concat(lastName, " ", firstName) as "Full Name", jobTitle from employees;

-- 4. offices 테이블에서 모든 사무실의 위치를 조회하세요.
select city from offices;

-- 5. orders 테이블에서 최근 10개의 주문을 조회하세요.
select * from orders order by orderDate desc limit 10;

-- 6. orderdetails 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
select * from orderdetails where orderNumber >= 10500;

-- 7. payments 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
select * from payments where customerNumber >= 495;

-- 8. productlines 테이블에서 각 제품 라인의 설명을 조회하세요.
select textDescription from productlines;

-- 9. customers 테이블에서 특정 지역의 고객을 조회하세요.
select * from customers where city like "a% City";

-- 10. products 테이블에서 특정 가격 범위의 제품을 조회하세요.
select * from products where buyPrice between 99 and 1000;

-- 중급
-- 1. orders 테이블에서 특정 고객의 모든 주문을 조회하세요.
select * from orders where customerNumber = 503;

-- 2. orderdetails 테이블에서 특정 제품에 대한 모든 주문 상세 정보를 조회하세요.
select * from orderdetails where productCode = "S99_0006"

-- 3. payments 테이블에서 특정 기간 동안의 모든 지불 정보를 조회하세요.
select * from payments where paymentDate between curdate() - 10 and curdate();

-- 4. employees 테이블에서 특정 직급의 모든 직원을 조회하세요.
select * from employees where jobTitle = "Sales Rep";

-- 5. offices 테이블에서 특정 국가의 모든 사무실을 조회하세요.
select * from offices where country = "Korea"

-- 6. productlines 테이블에서 특정 제품 라인에 속하는 모든 제품을 조회하세요.
select * from productlines where productLine = "Temp2"

-- 7. customers 테이블에서 최근에 가입한 5명의 고객을 조회하세요.
select * from customers order by customerNumber desc limit 5;

-- 8. products 테이블에서 재고가 부족한 모든 제품을 조회하세요.
select * from products where quantityInStock < 30;

-- 9. orders 테이블에서 지난 달에 이루어진 모든 주문을 조회하세요.
select * from orders where orderDate BETWEEN '2024-03-01' and '2024-03-31'

-- 10. orderdetails 테이블에서 특정 주문에 대한 총 금액을 계산하세요.
select sum(quantityOrdered * priceEach) from orderdetails where productCode = "S700_1938"

-- 고급
-- 1. customers 테이블에서 각 지역별 고객 수를 계산하세요.
select city, count(*) as customerCount from customers group by city;

-- 2. products 테이블에서 각 제품 카테고리별 평균 가격을 계산하세요.
select productLine, avg(buyPrice) from products group by productLine ;

-- 3. employees 테이블에서 각 부서별 직원 수를 계산하세요.
select officeCode, count(*) as "부서별 직원 수" from employees group by officeCode

-- 4. employees 테이블에서 각 사무실 별 평균 직원 연봉을 계산하세요.
select officeCode, avg(salary) from employees group by officeCode
-- 실제 employees에는 salary attribute 존재 X
