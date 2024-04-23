import pymysql


def init_connection():
    # 데이터베이스 연결 설정
    connection = pymysql.connect(
        host='localhost',  # 데이터베이스 서버 주소
        user='root',  # 데이터베이스 사용자 이름
        password='123123',  # 데이터베이스 비밀번호
        db='airbnb',  # 데이터베이스 이름
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


# 1. 새로운 제품 추가: Python 스크립트를 사용하여 'Products' 테이블에 새로운 제품을 추가하세요.
# 예를 들어, "Python Book"이라는 이름의 제품을 29.99달러 가격으로 추가합니다.
def problem_1(connection, cursor):
    sql = """
        INSERT INTO products (productID, productName, price, stockQuantity, createDate)
        SELECT '9', 'Python Book', 29.99, 100, NOW()
        FROM dual
        WHERE NOT EXISTS (
            SELECT 1 FROM products WHERE productID = '9'
        );
        """
    cursor.execute(sql)
    connection.commit()


# 2. 고객 목록 조회: 'Customers' 테이블에서 모든 고객의 정보를 조회하는 Python 스크립트를 작성하세요.
def problem_2(connection, cursor):
    sql = """
        SELECT * FROM customers
    """
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)


# 3. 제품 재고 업데이트: 제품이 주문될 때마다 'Products' 테이블의 해당 제품의 재고를 감소시키는 Python 스크립트를 작성하세요.
def problem_3(connection, cursor, target_product_sold_quantity, target_product):
    sql = """
    UPDATE products
    SET stockQuantity = stockQuantity - %s
    where productID = %s
    """
    cursor.execute(sql, (target_product_sold_quantity, target_product))
    connection.commit()


# 4. 고객별 총 주문 금액 계산: 'Orders' 테이블을 사용하여 각 고객별로 총 주문 금액을 계산하는 Python 스크립트를 작성하세요.
def problem_4(connection, cursor):
    sql = """
    SELECT customerID, sum(totalAmount) from orders
    group by customerID;
    """
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)


# 5. 고객 이메일 업데이트: 고객의 이메일 주소를 업데이트하는 Python 스크립트를 작성하세요.
# 고객 ID를 입력받고, 새로운 이메일 주소로 업데이트합니다.
def problem_5(connection, cursor, customer_id, modifying_email):
    sql = """
    UPDATE customers
    set email = %s
    where customerID = %s
    """
    cursor.execute(sql, (modifying_email, customer_id))
    connection.commit()


# 6. 주문 취소: 주문을 취소하는 Python 스크립트를 작성하세요.
# 주문 ID를 입력받아 해당 주문을 'Orders' 테이블에서 삭제합니다.
def problem_6(connection, cursor, order_id):
    sql = """
    DELETE FROM orders
    where orderID = '%s'
    """
    cursor.execute(sql, order_id)
    connection.commit()


# 7. 특정 제품 검색: 제품 이름을 기반으로 'Products' 테이블에서
# 제품을 검색하는 Python 스크립트를 작성하세요.
def problem_7(connection, cursor, product_name):
    sql = """
    SELECT * FROM products
    WHERE productName = '%s'
    """
    cursor.execute(sql, product_name)
    for row in cursor.fetchall():
        print(row)


# 8. 특정 고객의 모든 주문 조회: 고객 ID를 기반으로 그 고객의 모든 주문을 조회하는 Python 스크립트를 작성하세요.
def problem_8(connection, cursor, customer_id):
    sql = """
    SELECT * FROM orders
    WHERE customerID = '%s'
    """
    cursor.execute(sql, customer_id)
    for row in cursor.fetchall():
        print(row)


# 9. 가장 많이 주문한 고객 찾기: 'Orders' 테이블을 사용하여 가장 많은 주문을 한 고객을 찾는 Python 스크립트를 작성하세요.
def problem_9(connection, cursor):
    sql = """
    SELECT customerID, COUNT(*) AS orderCount
    FROM orders
    GROUP BY customerID
    ORDER BY orderCount DESC
    LIMIT 1;
    """
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)


def main():
    connection = init_connection()
    try:
        with connection:
            with connection.cursor() as cursor:
                problem_1(connection, cursor)
                problem_2(connection, cursor)
                problem_3(connection, cursor, '5', 'Python Book')
                problem_4(connection, cursor)
                problem_5(connection, cursor, '1', 'test@test.com')
                problem_6(connection, cursor, '1')
                problem_7(connection, cursor, 'Python Book')
                problem_8(connection, cursor, '2')
                problem_9(connection, cursor)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        connection.close()


if __name__ == '__main__':
    main()
