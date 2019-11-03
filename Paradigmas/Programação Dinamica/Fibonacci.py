def fib(n, f):
    print(f)
    f[0] = 0
    f[1] = 1

    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]

    print(f)
    return f[n]

f = [0,0,0,0,0,0]
print(fib(5, f))