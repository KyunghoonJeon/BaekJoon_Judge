import sys
input=sys.stdin.readline
n=int(input())
num_list=list(map(int,input().split()))
dp_up=[1 for i in range(n)]
dp_down=[1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if num_list[i]>num_list[j]:
            dp_up[i]=max(dp_up[i],dp_up[j]+1)
num_list.reverse()
for i in range(n):
    for j in range(i):
        if num_list[i]>num_list[j]:
            dp_down[i]=max(dp_down[i],dp_down[j]+1)
dp_down.reverse()
sum_list=[0]*n
for i in range(n):
    sum_list[i]=dp_up[i]+dp_down[i]
print(max(sum_list)-1)