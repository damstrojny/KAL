import random
import numpy as np
from random import randrange, getrandbits, randint
zad = int

while True:
    zad = int(input("\n[1] = suma \n[2] = xtime \n[3] = mnozenie \n[4] = odwrotnosc \nWprowadź numer zadania: "))


    def suma(a, b):
     c = hex(int(a, 16) ^ int(b, 16))[2:]
     return c

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

    def odwrotnosc(a):
     if a=="00" or a=="0":
         return "undefined"
     else:
         z=a
         y=[]
         for i in range (7):
             z=mnozenie(z,z)
             y[len(y):] = [z]
         x=y.pop()
         for i in range (6):
             z=mnozenie(z, y.pop())
         return z

    if zad == 1:
        print("\nPrzykładowe dane: \n")
        a = "a3"
        b = "f2"
        print("Dla a = a3, b = f2 wartość wyjściowa wynosi:",(suma(a,b)))
        a = "03"
        b = "1f"
        print("Dla a = 03, b = 1f wartość wyjściowa wynosi:",(suma(a,b)))
        a = input("\na = ")
        b = input("b = ")
        print(suma(a, b))

    if zad == 2:
        print("\nPrzykładowe dane: \n")
        a = "32"
        print("Dla a = 32, wartość wyjściowa wynosi:",(xtime(a)))
        a = "ff"
        print("Dla a = ff, wartość wyjściowa wynosi:",(xtime(a)))
        a = "bc"
        print("Dla a = bc, wartość wyjściowa wynosi:",(xtime(a)))
        a = input("\na = ")
        print(xtime(a))

    if zad == 3:
        print("\nPrzykładowe dane: \n")
        a = "02"
        b = "08"
        print("Dla a = 02, b = 08 wartość wyjściowa wynosi:",(mnozenie(a,b)))
        a = "ff"
        b = "e1"
        print("Dla a = ff, b = e1 wartość wyjściowa wynosi:",(mnozenie(a,b)))
        a = input("\na = ")
        b = input("b = ")
        print(mnozenie(a, b))

    if zad == 4:
        print("\nPrzykładowe dane: \n")
        a = "03"
        print("Dla a = 03, wartość wyjściowa wynosi:",(odwrotnosc(a)))
        a = "f0"
        print("Dla a = f0, wartość wyjściowa wynosi:",(odwrotnosc(a)))
        a = "00"
        print("Dla a = 00, wartość wyjściowa wynosi:",(odwrotnosc(a)))

        a = input("\na = ")
        print(odwrotnosc(a))
