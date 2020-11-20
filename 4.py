a = eval(input("n = "))
p = eval(input("b = "))

def power(x, y, z):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

def Qs(a, p):
    return power(a, (p - 1) // 2, p) == 1


print (Qs(a, p))