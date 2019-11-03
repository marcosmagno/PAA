def TrocaImpares(v, n, k):
    if n == 0:
        return v[n]
    soma = TrocaImpares(v, n-1, k)
    if v[n] % 2 != 0:
        soma = soma + 1
    if soma == k:
        v[n] = 0

v = [8,0,5,2,3,8,4,5,2]

print(TrocaImpares(v, len(v)-1, 2))