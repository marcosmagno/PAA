def findOddElement(arr):
    xor = 0
    for i in arr:
        xor = xor ^ i
        print(xor, i, xor ^i)
    
    return xor

arr = [ 2, 2, 1, 1, 6, 6, 2, 2, 4, 4, 6, 6, 1 ]
print(findOddElement(arr))

