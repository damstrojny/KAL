p = 1298074214633706907132624082305003
q = 1298074214633706907132624082304809
n = p*q
e = 1172187857271832809276226663461802240700459848485291886282435086085

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
    print("Klucz publiczny:")
    print ("n = ",n)
    print("d = ",d)
    print("Klucz tajny:")
    print ("n = ",n)
    print("e = ",e)