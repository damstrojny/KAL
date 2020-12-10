p = 1298074214633706907132624082305003
q = 1298074214633706907132624082304809
n = p*q
e = 1172187857271832809276226663461802240700459848485291886282435086085
m = 123456789

def euc(p, n):

    if n == 0:
        return (1, 0, p)
    q, r = p // n, p % n
    x, y, d = euc(n, r)
    s, t = y, x - q * y
    return s, t, d  

def inverse(p, n):

 return euc(p, n)[0]

phi = (p - 1) * (q - 1)
d = inverse(e, phi)






if(p != "" and q  != "" and e != ""):

 print("1) Generowanie klucza tajnego i publicznego\n2) Szyfrowanie\n3) Deszyfrowanie\n")
 g = input("Wprowadź liczbę: ")
 if(g=="1"): 
    print("Klucz publiczny:\nn = ",n,"\ne = ",e,"\nklucz tajny:\nn = ",n,"\nd = ",d)
 elif(g == "2"):
    print("in progress")
 elif(g == "3"):
    print("in progress")
   