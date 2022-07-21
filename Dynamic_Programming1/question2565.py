import sys
input=sys.stdin.readline
n=int(input())
wire_list=[]
for _ in range(n):
    wire_list.append(list(map(int,input().split())))
wire_list.sort()
dp=[1]*n
for i in range(n):
    for j in range(i):
        if wire_list[i][1]>wire_list[j][1]:
            dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))