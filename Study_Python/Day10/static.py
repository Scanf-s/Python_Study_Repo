class Person:
    population = 0  # static 멤버 변수

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1  # 모든 객체에 대해 공유되는 population을 증가시킴
    
    @staticmethod
    def is_adult(age):
        return age >= 18

# 객체 생성
person1 = Person("John", 30)
print(Person.population)  # 출력: 1

person2 = Person("Jane", 25)
print(Person.population)  # 출력: 2

# static 메소드 사용
print(Person.is_adult(20))  # 출력: True
print(Person.is_adult(16))  # 출력: False