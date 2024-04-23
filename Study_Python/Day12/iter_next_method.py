import random
for i in iter(lambda : random.randint(0, 5), 2):
    print(i, end=' ')

'''
it = iter(range(3))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
'''