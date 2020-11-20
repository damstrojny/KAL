b = eval(input("wpisz b: "))
k = eval(input("wpisz k: "))
n = eval(input("wpisz m: "))

def comp(b, k, m):
        ans = 1
        try:
            while k > 0:
                if (k & 1) == 1:
                    ans = (ans * b) % m
                k >>= 1
                b = (b * b) % m
            return ans
        except:
            raise


if __name__ == '__main__':

    x = comp(b, k, n)

    print(b,"^", k,"mod", n,"=", x)
