import sys
input=sys.stdin.readline
N=int(input())
def tile(n):
    dp=[0]*1000001
    dp[1],dp[2]=1,2
    for i in range(3,n+1):
        dp[i]=(dp[i-1]+dp[i-2])%15746
    return dp[n]
print(tile(N))