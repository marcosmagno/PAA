def seqAlternada(v, n, vetorSequencia):
    if n == 0:
        return v[n]
    
    d = seqAlternada(v, n-1, vetorSequencia)
    if v[n-2] > v[n -1] and v[n-1] < n :
        if v[n-2] not in vetorSequencia:
            vetorSequencia.append(v[n-2])
        if v[n-1] not in vetorSequencia:
            vetorSequencia.append(v[n-1])
        if v[n] not in vetorSequencia:
            vetorSequencia.append(v[n])
    if v[n-2] < v[n-1] and v[n-1] > v[n]:
        if v[n-2] not in vetorSequencia:
            vetorSequencia.append(v[n-2])
        if v[n-1] not in vetorSequencia:
            vetorSequencia.append(v[n-1])
        if v[n] not in vetorSequencia:
            vetorSequencia.append(v[n])
    return len(vetorSequencia), vetorSequencia

v = [4,3,2,5,8,7,1,10,11]
vectorS = []
print(seqAlternada(v, len(v)-1, vectorS))

