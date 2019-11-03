def fat(n):
    if n == 1:
        return 1
    print("n",n)
    return n * fat(n-1)


print(fat(4))