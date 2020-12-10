b = eval(input("wprowadz b: "))
n = eval(input("wprowadz n: "))


def euc(b, n):

    if n == 0:
        return (1, 0, b)
    q, r = b // n, b % n
    x, y, d = euc(n, r)
    s, t = y, x - q * y
    return s, t, d  

def inverse(b, N):

 return euc(b, N)[0]

print(inverse(b,n))
