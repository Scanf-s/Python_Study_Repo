-- 초급
-- 1. customers 테이블에 새 고객을 추가하세요.
insert into customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, country)
values (497, 'Scanf-s', 'Sullung', 'Yang', '123-456-7890', '123 Street', 'Some City', 'Some Country');
select * from customers;

-- 2. products 테이블에 새 제품을 추가하세요.
select * from products;
select * from productlines;
insert into products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
values ("S99_0000","TEMP PRODUCT", "Planes", "1:999", "Scanf-s", "Test data", 1000, 999.99, 99.99);

-- 3. employees 테이블에 새 직원을 추가하세요.
select * from employees;
insert into employees
values (2000, "Sullung", "Yang", "x9999", "temp@temp.com", 4, 1102, "Sales Rep");

-- 4. offices 테이블에 새 사무실을 추가하세요.
select * from offices;
insert into offices
values (8, "Seoul", "+82 10 0000 0000", "asdf Street", NULL, "Dongjak-Gu", "Korea", "00000", "NA");

-- 5. orders 테이블에 새 주문을 추가해주세요.
select * from orders;
insert into orders
values (99999, curdate(), curdate() + 1, NULL, "In Process", NULL, 497);

-- 6. orderdetails 테이블에 주문 상세 정보를 추가하세요.
select * from orderdetails;
insert into orderdetails
values (99999, "S99_0000", 99, 99.99, 2);
select * from orderdetails
where orderNumber = 99999;

-- 7. payments 테이블에 지불 정보를 추가하세요.
select * from payments;
insert into payments
values (497, "TEMP12345", curdate(), 99999.99);

-- 8. productlines 테이블에 제품 라인을 추가하세요.
select * from productlines;
insert into productlines
values ("Temp", "Temp Data", NULL, NULL);

-- 9. customers 테이블에 다른 지역의 고객을 추가하세요.
insert into customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, country)
values (498, 'Scanf', 'Sullung2', 'Yang', '123-456-7891', '124 Street', 'abc City', 'abc Country');
select * from customers;

-- 10. products 테이블에 다른 카테고리 제품을 추가하세요.
select * from products;
select * from productlines;
insert into products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
values ("S99_0001","TEMP PRODUCT 2", "Temp", "1:111", "Scanf", "Test data 2", 1500, 999.19, 89.99);

-- 중급
-- 1. customers 테이블에 여러 고객을 한 번에 추가하세요.
insert into customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, country)
values
	(499, 'tempuser1', 'temp1', 'User', '123-456-1111', '100 Street', 'aka City', 'Some Country'),
    (500, 'tempuser2', 'temp2', 'User', '123-456-1112', '101 Street', 'akb City', 'Some Country'),
    (501, 'tempuser3', 'temp3', 'User', '123-456-1113', '102 Street', 'akc City', 'Some Country');
select * from customers;

-- 2. products 테이블에 여러 제품을 한 번에 추가하세요.
select * from products;
insert into products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
values 
	("S99_0002","TEMP PRODUCT 2", "Planes", "1:999", "Scanf-s", "Test data 2", 1000, 999.99, 99.99),
    ("S99_0003","TEMP PRODUCT 2", "Planes", "1:999", "Scanf-s", "Test data 3", 1000, 999.99, 99.99),
    ("S99_0004","TEMP PRODUCT 2", "Planes", "1:999", "Scanf-s", "Test data 4", 1000, 999.99, 99.99);
    
-- 3. employees 테이블에 여러 직원을 한 번에 추가하세요.
select * from employees;
insert into employees
values
	(2001, "Sullung2", "Yang", "x9999", "temp2@temp.com", 4, 1102, "Sales Rep"),
    (2002, "Sullung3", "Yang", "x9999", "temp3@temp.com", 4, 1102, "Sales Rep"),
    (2003, "Sullung4", "Yang", "x9999", "temp4@temp.com", 4, 1102, "Sales Rep");
    
-- 4. orders와 orderdetails에 연결된 주문을 한 번에 추가하세요.
insert into orders
values (100000, curdate(), curdate() + 1, NULL, "In Process", NULL, 498);
select * from orders;
insert into orderdetails
values (100000, "S99_0001", 99, 99.99, 2);
select * from orderdetails
where orderNumber = 99999;

-- 5. payments 테이블에 여러 지불 정보를 한 번에 추가하세요alter
select * from payments;
insert into payments
values (498, "TEMP12346", curdate(), 99999.99),
(499, "TEMP12347", curdate(), 99999.99),
(500, "TEMP12348", curdate(), 99999.99);

-- 6. customers 테이블에 고객을 추가하고 바ㄹ로 주문을 추가하세요.
insert into customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, country)
values
	(502, 'tempuser4', 'temp4', 'User', '123-456-1114', '400 Street', 'akd City', 'Some Country');
insert into orders
values (100001, curdate(), curdate() + 1, NULL, "In Process", NULL, 502);
select customerNumber, customerName from customers where customerNumber = 502
union
select customerNumber, orderDate from orders where customerNumber = 502;

-- 7. employees 테이블에 직원을 추가하고 바로 직급을 할당하세요.
select * from employees;
insert into employees
values
	(2004, "Sullung4", "Yang", "x9999", "temp2@temp.com", 4, 1102, "NA");
update employees
set jobTitle = "Sales Manager (APAC)"
where employeeNumber = 2004;

-- 8. products 테이블에 제품을 추가하고 바로 재고를 업데이트하세요.
select * from products;
insert into products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
values 
	("S99_0005","TEMP PRODUCT 5", "Planes", "1:999", "Scanf-s", "Test data 5", 1000, 999.99, 99.99);
update products
set quantityInStock = 9999
where productCode = "S99_0005";

-- 9. offices 테이블에 새 사무실을 추가하고 바로 직원을 할당하세요.
insert into offices
values (9, "Seoul", "+82 10 0000 0001", "eeee Street", NULL, "Dongjak-Gu", "Korea", "00010", "NA");
update employees
set officeCode = 9
where employeeNumber = 2004;
select * from offices;
select * from employees where employeeNumber = 2004;

-- 10. productlines 테이블에 제품 라인을 추가하고 바로 여러 제품을 추가하세요
insert into productlines
values ("Temp2", "Temp Data 2", NULL, NULL);
select * from products;
update products
set productLine = "Temp2"
where productCode = "S99_0005";
select * from products where productCode = "S99_0005";

-- 고급
-- 1. customers 테이블에 새 고객을 추가하고 바로 주문을 추가하세요.
-- 2. employees 테이블에 새 직원을 추가하고 바로 그들의 매니저를 업데이터하세요.
-- 3. products 테이블에 새 제품을 추가하고 바로 그 제품에 대한 주문을 추가하세요.
-- 4. orders 테이블에 새 주문을 추가하고 바로 지불 정보를 추가하세요.
-- 5. orderdetails 테이블에 주문 상세 정보를 추가하고 바로 관련 제품의 재고를 감소시키세요.