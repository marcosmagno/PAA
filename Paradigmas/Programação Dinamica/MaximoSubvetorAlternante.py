def MaximoSubVetorAlternante(arr, n, las):
    
    resultado = 1


    for i in range(1, n):
        for j in range(0,i):
            print(i,j)
            if arr[j] < arr[i] and las[i][0] < las[j][1] +1:
                las[i][0] = las[j][1] + 1


            if arr[j] > arr[i] and las[i][1] < las[j][0] + 1:
                las[i][1] = las[j][0] + 1


    if res < max(las[i][0], las[i][1]):
        res = max(las[i][0], las[i][1])

    return res


arr= [ 10, 22, 9, 33, 49, 50, 31, 60 ] 
w, h = len(arr), 2
las = [[1 for x in range(w)] for y in range(h)]
print(las)


MaximoSubVetorAlternante(arr, len(arr), las)
