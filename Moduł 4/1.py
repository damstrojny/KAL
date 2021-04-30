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

a = "32"
print("Dla a = 32, wartość wyjściowa wynosi:",(xtime(a)))
a = "ff"
print("Dla a = ff, wartość wyjściowa wynosi:",(xtime(a)))
a = "bc"
print("Dla a = bc, wartość wyjściowa wynosi:",(xtime(a)))
  
a = input("wprowadz a: ")
print(xtime(a))


