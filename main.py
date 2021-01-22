def factOrSum(x,o):
    if o == "factorial":
        
        number= 1
        
        for i in range(1,x+1):
            number= number * i

        return number
    
    else:
        return
        
        sum = 0

        for i in range(0,x):
            sum = sum + 1
        
        
        return sum
        
        print(factOrSum(4,"factorial"))