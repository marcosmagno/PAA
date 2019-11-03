def contaVetores(v, n):
    if n == 0:
        return verificaPar(v[n], n)
    else:
        conta = contaVetores(v, n-1)
        soma = conta + verificaPar(v[n], n)
       
    return soma

def verificaPar(x, n):
    if x % 2 != 0:
        return 1
    else:
        return 0


v = [3,5,7,9,11]
print("resposta", contaVetores(v, len(v)-1))

