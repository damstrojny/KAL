def przeciwne(x, y, p):
    return x, p - y

p = eval(input("wpisz p: "))
x = eval(input("wpisz x: "))
y = eval(input("wpisz y: "))

x1, y1 = przeciwne(x, y, p)

print("Wyjście:")
print("x1 =", x1,"\ny1 =",y1)

