try:
    x = 10
    y = 0
    print(x / y)
    
    z = [1, 2, 3]
    print(z[4])
except ZeroDivisionError:
    print("0으로 나누면 안돼요")
except IndexError: #ZeroDivision에서 걸려가지고, 이건 실행 안됨
    print("접근하려는 배열 범위가 정상적인 범위를 넘어갔어요")
except: #위에서 에러가 처리되면, 아래쪽 except 구문은 실행 X
    print("예외 발생")


try:
    x = 10
    y = 2
    print(x / y)
except:
    print("예외발생")
else:
    print("실행 성공")
finally:
    print("무조건 실행되는 문장")