def iter_even():
    i = 0
    while True:
        yield i
        i += 2

def iter_odd():
    i = 1
    while True:
        yield i
        i += 2

def iter_power(k):
    i = 0
    while True:
        yield k ** i
        i += 1
