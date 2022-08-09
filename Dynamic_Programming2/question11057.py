import sys
input=sys.stdin.readline
n=int(input())
dp=[[0 for _ in range(10)] for _ in range(1001)]
for i in range(10):
    dp[1][i]=1
for i in range(10):
    dp[2][i]=i+1
for i in range(1001):
    dp[i][0]=1
for i in range(10):
    for j in range(3,1001):
        dp[j][i]=(dp[j-1][i]+dp[j][i-1])%10007
print(sum(dp[n])%10007)