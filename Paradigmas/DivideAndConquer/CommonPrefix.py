def commonPrefixUtil(str1, str2):  
  
    result = ""  
    n1, n2 = len(str1), len(str2) 
    i, j = 0, 0
    print(n1,n2)
    while i <= n1 - 1 and j <= n2 - 1:  
      
        if str1[i] != str2[j]:  
            break
        result += str1[i] 
        i, j = i + 1, j + 1
      
    return result 
  
# A Divide and Conquer based function to  
# find the longest common prefix. This is  
# similar to the merge sort technique  
def commonPrefix(arr, low, high):  
  
    if low == high: 
        return arr[low]  
  
    if high > low: 
      
        # Same as (low + high)/2, but avoids  
        # overflow for large low and high  
        mid = low + (high - low) // 2
  
        str1 = commonPrefix(arr, low, mid)  
        str2 = commonPrefix(arr, mid + 1, high)  
        print(str1, str2)
        return commonPrefixUtil(str1, str2)  
  
# Driver Code 
if __name__ == "__main__": 
  
    arr = ["geeksforgeeks", "geeks",  
                   "geek", "geezer"]  
    n = len(arr) 
    ans = commonPrefix(arr, 0, n - 1)  
  
    if len(ans):  
        print("The longest common prefix is", ans) 
    else: 
        print("There is no common prefix")  
  
# This code is contributed by Rituraj Jain 
