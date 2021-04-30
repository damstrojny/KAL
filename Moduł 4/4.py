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

def odwrotnosc(a):
    if a=="00" or a=="0":
        return 'undefined'
    else:
        wielomian=a
        y=[]
        for i in range (7):
            wielomian=mnozenie(wielomian,wielomian)
            y.append(wielomian)
        x=y.pop()
        for i in range (6):
            wielomian=mnozenie(wielomian, y.pop())
        return wielomian
      
  
a = "03"
print("Dla a = 03, wartość wyjściowa wynosi:",(odwrotnosc(a)))
a = "f0"
print("Dla a = f0, wartość wyjściowa wynosi:",(odwrotnosc(a)))
a = "00"
print("Dla a = 00, wartość wyjściowa wynosi:",(odwrotnosc(a)))

a = input("\nwprowadz a: ")

print(odwrotnosc(a))