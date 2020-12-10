
a = eval(input("a = "))
b = eval(input("b = "))

def power(x, y, z):
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number
  
def sqrt(a, b):  
  
    a = a % b  
    x = power(a, (b + 1) // 4, b)  
    if ((x*x) % b == a):  
        print(x)  
        return
    else:
      print ("not existing")
      return 


print (sqrt(a, b))
