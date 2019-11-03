def zzis(arr, n):

    las = [n][2]

    for i in range(0,n):
        las[i][0] = 1
        las[i][1] = 1

    res = 1

    for i in range(1,n):

        for j in range(0,n):

            if arr[j] < arr[i] and las[i][0] < las[j][1] + 1:
                las[i][0] = las[j][1] + 1

            if arr[j] > arr[i] and las[i][1] < las[j][0] + 1:
                las[i][j] = las[j][0] + 1
        
        if res < max(las[i][0], las[i][1]):
            res = max(las[i][0], las[i][1])

    return res

arr = [10, 22, 9, 33, 49, 50, 31, 60]
print(zzis(arr,len(arr) -1))