# Python3 program to calculate pow(x,n) 
  
# Function to calculate x 
# raised to the power y  
def power(x, y): 
    if (y == 0):
        print("return")
        return 1
    elif (int(y % 2) == 0):
        print(power(x, int(y / 2)),power(x, int(y / 2)), "result", power(x, int(y / 2)) *  power(x, int(y / 2)))
        return (power(x, int(y / 2)) *  power(x, int(y / 2))) 
    else: 
        print(x * power(x, int(y / 2)),power(x, int(y / 2)), "result", x * power(x, int(y / 2)) * power(x, int(y / 2)))
        return (x * power(x, int(y / 2)) * power(x, int(y / 2))) 
  
# Driver Code 
x = 2; y = 3
print(power(x, y,)) 
