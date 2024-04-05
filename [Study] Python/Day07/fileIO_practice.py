f = open("D:\\Dev\\Workspace\\OZ_Backend\\OZCoding_Backend\\[Study] Python\\Day7\\input.txt", "a")
# "a" -> 추가 쓰기 모드
# "w" -> 새로 쓰기 모드

for i in range(10):
    f.write("Hello\n")

f.close()