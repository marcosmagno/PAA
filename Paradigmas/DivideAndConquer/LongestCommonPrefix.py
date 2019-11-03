def findLCP(words, low, high):
    # caso base: 
    if low > high:
        return " "
    
    if low == high:
        return words[low]
    
    # find de mid index
    mid = (low + high) // 2
    X = findLCP(words, low, mid)
    Y = findLCP(words, mid+1 , high)
    return LCP(X,Y)

def LCP(X, Y):
    print(X, Y)
    i = 0
    j = 0
    while(i < len(X) and j < (len(Y))):
        if(X[i] != Y[j]):
            break
        i = i + 1
        j = j + 1
        print(i,j)
    return X[:i]

words = ["marcos", "mar", "maraberto","marcarrao"]
print("Fim", findLCP(words,0, len(words)-1))