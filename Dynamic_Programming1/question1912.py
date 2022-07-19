import sys
input=sys.stdin.readline
N=int(input())
temp=list(map(int,input().split()))
dp=[0]*N
dp[0]=temp[0]
for i in range(1,N):
    dp[i]=max(temp[i],dp[i-1]+temp[i])
print(max(dp))