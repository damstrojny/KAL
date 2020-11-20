a = eval(input("n = "))
p = eval(input("b = "))

def QR(a, p):
    return pow(a, (p - 1) // 2, p) == 1


print (QR(a, p))