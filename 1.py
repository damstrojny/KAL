import random 
  
def random_length(p): 
    
    value = "" 
    for i in range(p): 

        temp = str(random.randint(0, 1)) 
  
        value += temp 

    return(value) 
  
if __name__ == "__main__":
    print(int(random_length(3),2))
    print(int(random_length(15),2))
    print(int(random_length(7),2))
    print(int(random_length(55),2))