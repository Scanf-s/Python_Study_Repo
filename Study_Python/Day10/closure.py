def calc():
    a = 3
    b = 5
    return lambda x : a * x + b      # 람다식으로 이루어진 익명함수 반환
 
c = calc() # 클로져 호출
print(c(1), c(2), c(3), c(4), c(5)) 

def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add
 
c = calc()
c(1)
c(2)
c(3)