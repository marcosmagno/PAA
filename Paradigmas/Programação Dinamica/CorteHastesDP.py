"""
# A Dynamic Programming solution for Rod cutting problem 
INT_MIN = -32767
  
# Returns the best obtainable price for a rod of length n and 
# price[] as prices of different pieces 
def cutRod(price, n): 
    val = [0 for x in range(n+1)] 
    val[0] = 0
  
    # Build the table val[] in bottom up manner and return 
    # the last entry from the table 
    for i in range(1, n+1): 
        max_val = INT_MIN 
        for j in range(i): 
             max_val = max(max_val, price[j] + val[i-j-1]) 
        val[i] = max_val 
  
    return val[n] 
"""
INT_MIN = -32767
def Memoized_CutRoad(p, n):
    val = [0 for x in range(0, n+1)]
    return Memoized_CutRoad_Aux(p,n,val)


def Memoized_CutRoad_Aux(p,n,val):
    if val[n] > 0:
        # ja existe o valor calculado
        return val[n]
    if n == 0:
        max_val = 0
    else:
        max_val = INT_MIN
        print(n)
        for i in range(0,n):
            max_val = max(max_val, p[i] + Memoized_CutRoad_Aux(p, n-i-1, val))
            #print(i, n, max_val, p[i], Memoized_CutRoad_Aux(p, n-i-1, val))
        val[n] = max_val
    return max_val

arr = [1,5,8,9] 
size = len(arr) 
print("Maximum Obtainable Value is", Memoized_CutRoad(arr, size)) 