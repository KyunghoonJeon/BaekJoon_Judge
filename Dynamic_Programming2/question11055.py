import sys
input=sys.stdin.readline
n=int(input())
num_list=list(map(int,input().split()))
dp=num_list[:]
print(dp)
for i in range(1,n):
    for j in range(i):
        if num_list[i]>num_list[j]:
            dp[i]=max(num_list[j]+dp[i], dp[i])
print(max(dp))