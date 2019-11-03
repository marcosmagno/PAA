def contaVetores(v,low, high):
    if low == high:
        return verificaPar(v[low])
    mid = (low + high) // 2
    getReturnLeft = contaVetores(v, mid, high)
    gerReturnRight = contaVetores(v, mid + 1, high)

    return getReturnLeft + gerReturnRight



def verificaPar(v):
    if v % 2 == 0:
        return 1 
    else:
        return 0


v = [8,0,5,4,3,8,4,5,2]
print("FIM", contaVetores(v,0, len(v) - 1))

"""
def contaVetores(v, n):
    if n == 0:
        return verificaPar(v[n], n)
    else:
        conta = contaVetores(v, n-1)
        print("Soma" , n, v[n])
        soma = conta + verificaPar(v[n], n)
    return soma

def verificaPar(x, n):
    if x % 2 == 0:
        return 1
    else:
        return 0


v = [8,0,5,4,3,8,4,5,2]
print("resposta", contaVetores(v, len(v)-1))


def somaVetor(v, n):
    if n == 0:
        return v[n]
    else:
        soma = v[n] + somaVetor(v, n-1)
    return soma

v = [1,2,3]

print(somaVetor(v, len(v)-1))



def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])


print(listsum([1,3,5,7,9]))
"""