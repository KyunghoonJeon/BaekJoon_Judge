import sys
INF=10**9
input=sys.stdin.readline
n=int(input())
answer=INF
color=[]
for _ in range(n):
    color.append(list(map(int,input().split())))
for i in range(3):
    dp=[[INF,INF,INF] for _ in range(n)]
    dp[0][i]=color[0][i]
    for j in range(1,n):
        dp[j][0]=min(dp[j-1][1],dp[j-1][2])+color[j][0]
        dp[j][1]=min(dp[j-1][0],dp[j-1][2])+color[j][1]
        dp[j][2]=min(dp[j-1][0],dp[j-1][1])+color[j][2]
    for j in range(3):
        if i!=j:
            answer=min(answer,dp[-1][j])
print(answer)