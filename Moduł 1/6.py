import random

n = eval(input("n = "))

def prime(n):
    if n == 1: return False
    if n == 2: return True
    for k in range(100):
        a = random.randint(2, n - 1)
        if nwd(n, a) != 1:
            return False
        if pow(a, n - 1, n) != 1:
            return False
    return True

def nwd(x, y):
    while y > 0:
        a, y = y, x % y
    return a

print(prime(n))