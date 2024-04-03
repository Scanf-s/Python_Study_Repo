def plus_ten(x):
    return x + 10

result = list(map(plus_ten, [1, 2, 3])) #람다를 사용하지 않는 경우
result2 = list(map(lambda x : x + 10, [1, 2, 3])) #람다를 사용하는 경우
print(result)
print(result2)

# 만약, integer 리스트에서 짝수 요소만 뽑아버리고 싶다면..
mylist = [1, 2, 3, 4, 5]
myEvenList = list(filter(lambda x: x % 2 == 0, mylist))
print(myEvenList)

def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x # 가장 가까이 존재하는 x를 탐색 (여기서는 B의 지역변수 x가 됨)
            nonlocal y # 가장 가까이 존재하는 y를 탐색 (여기서는 A의 지역변수 y가 됨)
            """
            nonlocal z # 파이썬 인터프리터가 z를 상위에서 찾는데, 
            없으므로 빨간줄이 그임
            """
            z = 10
            x = x + 30
            y = y + 300
            print("In C() : ", x) # B의 지역변수 x -> 50 출력
            print("In C() : ", y) # A의 지역변수 y -> 400 출력
            print("In C() : ", z) # C의 지역 변수 z -> 10 출력
        C()
        print("In B() : ", x) # B의 지역 변수 x 호출 (그런데 C에서 이미 변경되었으므로 50 출력)
        print("In B() : ", y) # 
    B()
    print("In A() : ", x) # A의 지역변수 x -> 10 출력
    print("In A() : ", y) # A의 지역변수 x -> 400 출력
A()