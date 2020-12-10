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



def generate_keys(key): 
    p = generate_prime(key)
    q = generate_prime(key)
    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randrange(2 ** (key - 1), 2 ** key - 1)
        if is_CoPrime(e, phi):
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

def is_CoPrime(d, Phi):  
    return nwd(d, Phi) == 1

def generate_prime(keysize):  
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if isPrime(num):
            return num
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


def encrypt(e, n, msg):  
    cipher = ""
    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, n)) + " "

    return cipher


def decrypt(d, n, cipher): 
    msg = ""
    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, n))

    return msg


if __name__ == '__main__':
    KeySize = 16
    p, q, n, pn, e, d = generate_keys(KeySize)
    
    print("Klucz publiczny:\nn = ",n,"\ne = ",e,"\nKlucz tajny:\nn = ",n,"\nd = ",d,"\n")

    
              
print ("                     #####SZYFROWANIE#####\n")
print("e:",e)
print("n:",n)
msg = input("Wprowadź wiadomość do zaszyfrowania: ")
enc = encrypt(e, n, msg)
print("\nZaszyfrowana wiadomość: ",enc,"\n")
print ("                    #####DESZYFROWANIE#####\n")
print("d: ",d)
print("n: ",n,"\n")
msg = input("Wprowadź wiadomość do odszyfrowania: ")
dec = decrypt(d, n, msg)
print("Odszyfrowana wiadomość: ",dec)
           