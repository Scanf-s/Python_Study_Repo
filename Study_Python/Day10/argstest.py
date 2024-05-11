def custom_print(*args, sep=' ', end='\n'):
    """
    가변 인수와 함께 sep, end 키워드 인자를 사용하여 문자열을 출력하는 함수.
    기본값으로 sep과 end의 값을 지정해주고, 
    사용자가 이 값을 입력하지 않았다면, 기본값으로 설정
    
    :param args: 출력할 값들(가변 인수).
    :param sep: 출력되는 값들 사이에 사용할 구분자. 기본값은 공백(' ').
    :param end: 출력의 끝에 추가할 문자열. 기본값은 줄바꿈('\n').
    """
    output = sep.join(str(arg) for arg in args)
    output += end
    print(output, end='')

# 함수 사용 예시
custom_print('이것은', 'custom_print', '함수의', '예제입니다.', sep = "...", end=',\n')

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)

dict = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='', end=' ')

personal_info(name='홍길동')
print('\n')
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
print('\n')

#Dictionary를 넣는경우
personal_info(**dict)