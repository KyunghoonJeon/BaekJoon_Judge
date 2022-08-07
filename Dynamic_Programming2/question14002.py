import sys
input=sys.stdin.readline
n=int(input().rstrip())
num_list=list(map(int,input().split()))
dp=[1]*n
for i in range(n):
    for j in range(i):
        if num_list[i]>num_list[j]:
            dp[i]=max(dp[i], dp[j]+1)
print(dp)

res=[]
curr=max(dp)
for i in range(n-1,-1,-1):
    if dp[i]==curr:
        res.append(num_list[i])
        curr-=1
res.reverse()
print(*res)