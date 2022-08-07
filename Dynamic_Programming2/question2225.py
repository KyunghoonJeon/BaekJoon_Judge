import sys
input=sys.stdin.readline
n,k=map(int,input().split())
dp=[[0]*(201) for i in range(201)]
for i in range(201):
    dp[0][i]=1
for i in range(201):
    for j in range(201):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(dp[k-1][n])