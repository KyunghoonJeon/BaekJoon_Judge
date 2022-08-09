import sys
input=sys.stdin.readline
t=int(input())
dp=[0,1,2,4]
for _ in range(t):
    n=int(input())
    for i in range(len(dp),n+1):
        dp.append((dp[-1]+dp[-2]+dp[-3])%1000000009)
    print(dp[n])