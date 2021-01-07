import random


def generate(p):
    a = random.randint(2, p)
    b = random.randint(2, p)
    return a, b


p = eval(input("wpisz p: "))
print("p =", p,"\n")
a, b = generate(p)
print("A =", a,"\nB =", b)

