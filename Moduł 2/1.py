import random

def binpow(x, y, z):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

def generate(p):
    a = random.randint(2, p)
    b = random.randint(2, p)
    return a, b


p = 68719476731

print("p =", p,"\n")
a, b = generate(p)
print("A =", a)
print("B =", b)

