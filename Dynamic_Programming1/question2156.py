import sys
input=sys.stdin.readline
s=[]
dp=[0]*10000
n=int(input())
for i in range(n):
    s.append(int(input()))
dp[0]=s[0]
dp[1]=s[0]+s[1]
dp[2]=max(s[1]+s[2],s[0]+s[2],dp[1])
for j in range(3,n):
    dp[j]=max(dp[j-3]+s[j-1]+s[j],dp[j-2]+s[j],dp[j-1])
print(max(dp[n-1],dp[n-2]))