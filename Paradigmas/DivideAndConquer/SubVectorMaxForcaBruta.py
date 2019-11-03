def maximumsubarray(arr, n):
    maxsum = 0

    for i in range(0,n):
        sum = 0
        for j in range(i,n):
            print("arrj", arr[j])
            
            sum = sum + arr[j]
            print("sum", sum)
            if sum >= maxsum:
                maxsum = sum
                print("max", maxsum)

    return maxsum


arr = [-2,-4,8,4,3,3,-9]

print(maximumsubarray(arr, len(arr)))