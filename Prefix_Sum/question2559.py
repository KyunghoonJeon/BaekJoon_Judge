import sys
input=sys.stdin.readline
N,K=map(int,input().split())
temp=list(map(int,input().split()))
first=0
sum_list=[first]
for i in range(N):
    first+=temp[i]
    sum_list.append(first)
day_list=[]
for j in range(N-K+1):
    day_list.append(sum_list[j+K]-sum_list[j])
print(max(day_list))