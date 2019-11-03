def mimim(a,b):
    if a < b:
        return a
    else:
        return b


def troco(T, vetorNotas, dp):

    if T == 0:
        return 1
    else:
        if dp[T] != -1:
            return dp[T]
        
    if T < 0:
        return 100000

    
    else:
        temp = troco(T-vetorNotas[0], vetorNotas, dp)
        for i in range(1, len(vetorNotas)):
            temp = mimim(temp, troco(T-vetorNotas[i], vetorNotas, dp))
            dp[T] = temp + 1
    return dp[T]
T = 16
v = [1,2,5,10]
dp = [-1 for i in range(0,(T+1))]


print(dp)
print(troco(T,v, dp))

