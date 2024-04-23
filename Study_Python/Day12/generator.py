import random
def number_generator():
    yield "크아악" # yeild를 사용하면 함수는 제너레이터가 되며, yeild에는 값(변수)를 지정해서 사용하면 된다
    yield "파이썬?파이선?" # 해당 값을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 맡김
    yield 123123

    return "더 이상 yield 값이 존재하지 않습니다" # StopIteration 예외 처리

for i in number_generator(): # 제너레이터도 이터레이터이기 때문에, __iter__와 __next__ 존재
    print(i)


try:
    g = number_generator() # 제너레이터의 첫 yield 실행
    a = next(g) # yield를 사용하여 함수 바깥으로 전달한 값(0)이 next의 반환값으로 나오게 됨
    print(a)

    b = next(g)
    print(b)

    c = next(g)
    print(c)

    d = next(g) # StopIter Exception 발생
    print(d)
except StopIteration as e:
    print(e)


def my_generator(strArr):
    for str in strArr:
        yield str.upper()
    return "작업 끝"

strArr = ["asdf", "fghfds", "iodigjo"]
for i in my_generator(strArr): # 사용자 정의 generator
    print(i)


# 여러개의 요소를 한번에 바깥으로 내보내려면 ?
# yield from 원하는객체 <<<<를 사용한다
def number_generator():
    numArr = random.sample(range(1, 10), 3) # 1~10까지 숫자중 3개 랜덤하게 선택
    yield from numArr

for i in number_generator():
    print(i)


# 제너레이터 표현식
arr1 = [i for i in range(50) if i % 2 == 0]
arr2 = (i for i in range(50) if i % 2 == 0)
print(arr1)
print(arr2)