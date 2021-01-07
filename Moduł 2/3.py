def aa(a, b, p, x, y):
    if (((x*x*x) + (a*x) + b) - (y * y)) % p == 0:
        return True
    else:
        return False

print("Przykład 1")
p = 68719476731
a = 49710749469
b = 5286130045
x = 12520181851
y = 51057687062
print("Wyjście:")
print(aa(a, b, p, x, y),"\n")

print("Przykład 2")
p = 68719476731
a = 49710749469
b = 5286130045
x = 12520181851
y = 51057687000
print("Wyjście:")
print(aa(a, b, p, x, y),"\n")

print("Przykład 3")
p = 83076749736557242056487941267521467
a = 51966339240643817679159456819110758
b = 69222991666392733393816378184919461
x = 3907170373
y = 4656627897
print("Wyjście:")
print(aa(a, b, p, x, y),"\n")

print("Przykład 4")
p = 7
a = 2
b = 4
x = 6
y = 1
print("Wyjście:")
print(aa(a, b, p, x, y))