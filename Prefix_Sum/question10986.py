import sys
N,M=map(int, sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
first=l[0]
sum_list=[first]
for i in range(1,N):
    first+=l[i]
    sum_list.append(first)
rem_list=[0]*M
for i in range(N):
    rem_list[sum_list[i]%M]+=1
first=rem_list[0]
cnt=first+first*(first-1)/2
for j in range(1,M):
    cnt+=rem_list[j]*(rem_list[j]-1)/2
print(int(cnt))
