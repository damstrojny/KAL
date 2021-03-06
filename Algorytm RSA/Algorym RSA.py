import random

#zad 6
def primef(n,d):
    if n == 1: return False
    if n == 2: return True
    for k in range(100):
        a = random.randint(2, n - 1)
        if nwd(n, a) != 1:
            return False
        if pow(a, n - 1, n) != 1:
            return False
    return True

def nwd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def gpkeys(key): 
  p = gprime(key)
  q = gprime(key)
  n = p * q
  phi = (p - 1) * (q - 1)

  while True:
      e = random.randrange(2 ** (key - 1), 2 ** key - 1)
      if is_coPrime(e, phi):
          break

  d = inverse(e, phi)
  return p, q, n, phi, e, d

def isPrime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True   

def is_coPrime(d, phi):  
    return nwd(d, phi) == 1

def gprime(pqsize):  
    while True:
        randnum = random.randrange(2 ** (pqsize - 1), 2 ** pqsize - 1)
        if isPrime(randnum):
            return randnum
#zad 2
def euc(b, n):

    if n == 0:
        return (1, 0, b)
    q, r = b // n, b % n
    x, y, d = euc(n, r)
    s, t = y, x - q * y
    return s, t, d  

def inverse(b, n):

 return euc(b, n)[0]


def encrypt(e, n, m):  
    code = ""
    for i in m:
        m = ord(i)
        code += str(pow(m, e, n)) + " "
    return code


def decrypt(d, n, code): 
    m = ""
    parts = code.split()
    for part in parts:
        if part:
            i = int(part)
            m += chr(pow(i, d, n))
    return m


if __name__ == '__main__':
  pqsize = 16
  p, q, n, pn, e, d = gpkeys(pqsize)
  print ("p =",p,"q =",q,"\n")  
  print("Klucz publiczny:\nn = ",n,"\ne = ",e,"\nKlucz tajny:\nn = ",n,"\nd = ",d,"\n")

                
print ("                     #####SZYFROWANIE#####\n")
print("e:",e)
print("n:",n)
m = input("Wprowadź wiadomość do zaszyfrowania: ")
enc = encrypt(e, n, m)
print("\nZaszyfrowana wiadomość: ",enc,"\n")
print ("                    #####DESZYFROWANIE#####\n")
print("d: ",d)
print("n: ",n,"\n")
m = input("Wprowadź wiadomość do odszyfrowania: ")
dec = decrypt(d, n, m)
print("Odszyfrowana wiadomość: ",dec)
           