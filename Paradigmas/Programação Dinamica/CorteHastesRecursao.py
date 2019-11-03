"""
def Cut_Rod(p,n):
    if n == 0:
        return 0
    q = -1
    for i in range(1,n-1):
        q = max(q, p[i] + Cut_Rod(p, n-1))

    return q


p = [1,5,8,9]
print(Cut_Rod(p, 4))
"""

import sys 


def cutRod(price, n): 
    if(n == 0): 
        return 0
    max_val = -10000

    for i in range(0, n): 
        max_val = max(max_val, price[i] + cutRod(price, n - i - 1)) 
    return max_val 
  
# Driver code 
arr = [1,5,8,9] 
size = len(arr) 
print("Maximum Obtainable Value is", cutRod(arr, size)) 
  
# This code is contributed by 'Smitha Dinesh Semwal' 
