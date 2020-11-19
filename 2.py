def mi(a, m): 
    mod0 = m 
    y = 0
    x = 1
    if (m == 1): 
        return 0
    while (a > 1):
        q = a // m 
        t = m 
        m = a % m 
        a = t 
        t = y 
        y = x - q * y 
        x = t 
    if (x < 0): 
        return x + mod0 
    return x 
  

if __name__ == "__main__":
    print(mi(25, 4))
    print(mi(15, 122))
    print(mi(11, 37))