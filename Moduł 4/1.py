def suma(a, b):
    c = hex(int(a, 16) ^ int(b, 16))[2:]
    return c

a = "a3"
b = "f2"
print("Dla a = a3, b = f2 wartość wyjściowa wynosi:",(suma(a,b)))

a = "03"
b = "1f"
print("Dla a = 03, b = 1f wartość wyjściowa wynosi:",(suma(a,b)))

a = input("\nwprowadz a: ")
b = input("wprowadz b: ")
print(suma(a,b))