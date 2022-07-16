import sys
input=sys.stdin.readline
N,M=map(int, input().split())
num=list(map(int,input().split()))
# new_num=[0]*(N+1)
# for j in range(1,N+1):
#     new_num[j]=new_num[j-1]+num[j-1]
# for i in range(M):
#     a,b=map(int,input().split())
#     print(new_num[b]-new_num[a-1])
first=0
sum_list=[first]
for i in range(N):
    first+=num[i]
    sum_list.append(first)
for i in range(M):
    a,b=map(int,input().split())
    print(sum_list[b]-sum_list[a-1])