"""
com DP
"""
dp =[-1,-1,-1,-1,-1,-1,-1,-1]
import time
def solve(n):  

    if n < 0:
        return 0
    if (n == 0):
        return 1

    if dp[n] != -1:
        return dp[n]
    dp[n] = solve(n-1) + solve(n-3) + solve(n-5)
    return dp[n]

print(solve(7))

