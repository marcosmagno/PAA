def maiorElemento(v, n):
    print(n)
    if n == 0:
        return v[0]
    x = maiorElemento(v, n-1)
    if x > v[n]:

        return x
    else:
        return v[n]


v = [13,-3,-25,20,-3,-16,-23]
print(maiorElemento(v, 5))
#for i in v:
#    print(maiorElemento(v,i))