    table=[[None]*(n+1) for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                table[i][j]=0
            elif x[i-1]==y[j-1]:
                table[i][j]=1+table[i-1][j-1]
            else:
                table[i][j]=max(table[i-1][j],table[i][j-1])
    return table[m][n]


for _ in range(int(input())):
    s=input()
    l=len(s)
    rev=s[::-1]
    curr=lcs(s,rev)
    need=l-curr
    print(need)

