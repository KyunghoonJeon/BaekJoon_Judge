import sys
import math
input=sys.stdin.readline
# n=int(input())
# dp=[k for k in range(n+1)]

# for i in range(1,n+1):
#     for j in range(1,i):
#         if j**2>i:
#             break
#         else:
#             dp[i]=min(dp[i-j**2]+1, dp[i])
# print(dp[n])

n=int(input())
dp=[i for i in range(n+1)]
for i in range(1,n+1):
    tmp=[]
    for j in range(1,i):
        if j*j>i:
            break
        tmp.append(dp[i-j*j])
    if tmp:
        dp[i]=min(tmp)+1
print(dp[n])

n = int(input())
dp = [x for x in range (n+1)]
for i in range(1,n+1):
    for j in range(1,i):
        if j*j > i :
            break
        if dp[i] > dp[i-j*j] + 1 :
            dp[i] = dp[i-j*j] + 1
print(dp[n])