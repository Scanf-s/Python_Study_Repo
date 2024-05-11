class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self # 자신의 주소 반환
    
    def __next__(self):
        if self.current < self.stop:
            num = self.current # 반환할 숫자
            self.current += 1
            return num
        else:
            raise StopIteration
        
    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError

for i in Counter(3):
    print(i, end = ' ') #range()와 똑같이 생성된다.
print('\n')
a, b, c, d, e = Counter(5) # iterator unpacking
print(a, b, c, d, e ,sep = "..")

# 특정 반환값을 할당하고 싶지 않은 경우 (무시하고 싶은 경우) 언더바를 사용한다.
a, _, c, d, _ = Counter(5) # iterator unpacking
print(a, c, d)