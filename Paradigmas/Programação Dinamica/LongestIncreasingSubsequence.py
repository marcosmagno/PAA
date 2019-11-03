# Dynamic programming Python implementation of LIS problem 
  
# lis returns length of the longest increasing subsequence 
# in arr of size n 
def lis(arr): 
    n = len(arr) 
    # Declare the list (array) for LIS and initialize LIS 
    # values for all indexes 
    lis = [1]*n 
    print(lis)

    maxminum = 0
    # Compute optimized LIS values in bottom up manner 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] =  max(maxminum, lis[i]+1)
                maxminum = lis[j]+1
  
    # Initialize maximum to 0 to get the maximum of all 
    # LIS 
    
  
    # Pick maximum of all LIS values 
    #for i in range(n): 
    #    maximum = max(maximum , lis[i]) 
    print(lis)
    return maxminum 
# end of lis function 
  
# Driver program to test above function 
arr = [10, 22, 9, 33, 49, 50, 31, 60] 
print("Length of lis is", lis(arr))
# This code is contributed by Nikhil Kumar Singh 
