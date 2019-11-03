
# A Divide and Conquer based program 
# for maximum subarray sum problem 
  
# Find the maximum possible sum in 
# arr[] auch that arr[m] is part of it 
def maxCrossingSum(arr, l, m, h) : 
      
    # Include elements on left of mid. 
    sm = 0; left_sum = -10000
     # 0 0 1 
    for i in range(m, l-1, -1) :

        sm = sm + arr[i] 
      
        if (sm > left_sum) : 
            left_sum = sm 
      
      
    # Include elements on right of mid 
    sm = 0; right_sum = -1000
    for i in range(m + 1, h + 1) : 
        sm = sm + arr[i] 

        if (sm > right_sum) : 
            right_sum = sm 
      
  
    # Return sum of elements on left and right of mid 
    return left_sum + right_sum; 
  
  
def maxSubArraySum(arr, l, h, debug) : 
    if (l == h) :
        return arr[l] 
  
    m = (l + h) // 2
    resultLeft = maxSubArraySum(arr, l, m, "left")
    resultRight = maxSubArraySum(arr, m+1, h, "right")
    resultCrossing = maxCrossingSum(arr, l, m, h)
    d = max(resultLeft, resultRight, resultCrossing)
    return d

  
# Driver Code 
#arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7] 
arr = [-2, -5, 6, -2, -3, 1, 5, -6]
n = len(arr) 
max_sum = maxSubArraySum(arr, 0, n-1, "init") 
print("Maximum contiguous sum is ", max_sum) 
  
# This code is contributed by Nikita Tiwari. 
