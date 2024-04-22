import itertools
import random
def A(iteratorA=itertools.cycle('01')):
    return next(iteratorA)

for x in range(10):
    n = A()
    print(n)

print('-----')

def iteratorB():
    while True:
        yield random.choice([0, 1])

for x in range(10):
    n = iteratorB()
    print(next(n))

print('-----')

def C(iteratorC=itertools.cycle([0, 1, 0, -1])):
    return next(iteratorC)

for x in range(10):
    n = C()
    print(n)
