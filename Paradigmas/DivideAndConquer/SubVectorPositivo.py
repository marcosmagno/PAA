def contaVetores(v,low, high):
    if low == high:
        return verificaPar(v[low])

    mid = (low + high) // 2
    getReturnLeft = contaVetores(v, low, mid)
    gerReturnRight = contaVetores(v, mid + 1, high)

    return getReturnLeft + gerReturnRight



def verificaPar(v):
    if v % 2 == 0:
        return 1 
    else:
        return 0


v = [1,3,5,4,6,8,10,12]
print("FIM", contaVetores(v,0, len(v) - 1))
