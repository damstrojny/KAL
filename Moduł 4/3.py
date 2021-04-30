def suma(a, b):
    c = hex(int(a, 16) ^ int(b, 16))[2:]
    return c

def xtime(a):
    a=bin(int(a, 16))[2:]
    if len(a)<=7:
        a=a+'0'
        a=hex(int(a,2))[2:]
    elif len(a)>7:
        a=a[1:9]
        a=a+'0'
        a=hex(int(a,2))[2:]
        a=suma(a,"1B")
    return a

def mnozenie(a,b):
    x=0
    y=b
    a=bin(int(a, 16))[2:]
    dlugosc=len(a)
    for i in range(dlugosc):
        y=b
        if a[i]=='1':
            c=dlugosc-1-i
            while c>0:
                y=xtime(y)
                c=c-1
            x=suma(y, str(x))
    return x
a = "02"
b = "08"
print("Dla a = 02, b = 08 wartość wyjściowa wynosi:",(mnozenie(a,b)))

a = "ff"
b = "e1"
print("Dla a = ff, b = e1 wartość wyjściowa wynosi:",(mnozenie(a,b)))

a = input("\nwprowadz a: ")
b = input("wprowadz b: ")
print(mnozenie(a,b))