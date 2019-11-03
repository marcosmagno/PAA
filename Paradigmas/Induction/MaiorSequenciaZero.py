def min(a,b):
    if a < b:
        return a
    else:
        return b

def MaiorSegZero(v, n):
    # Caso base
    if n == 0:
        if v[n] == 0:
            return (1,1)

    else:
        maioTamanho, tamanhoAtual = MaiorSegZero(v, n-1)
        if v[n] == 0:
            tamanhoAtual += 1
        else:
            tamanhoAtual = 0
        
        if tamanhoAtual > maioTamanho:
            maioTamanho = tamanhoAtual
        return (maioTamanho,tamanhoAtual)

v = [0,0,0,0,1,1,1]
print(MaiorSegZero(v, len(v)-1))
