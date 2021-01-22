def factOrSum(x,o):
    if o == "factorial":
        
        number = 1
        
        for i in range(1, x + 1):
            number= number * i

        return number


    else:


     add = 0 
     
     for i in range(0, x + 1):
            add = add + i   

     return add
        
    
print(factOrSum(4,"factorial"))