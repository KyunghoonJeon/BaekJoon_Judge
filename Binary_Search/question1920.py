import sys
input=sys.stdin.readline

#집합 쓰는 방법(효율은 훨씬 좋다)
n=int(input())
num_list=set(map(int, input().split()))
m=int(input())
target_list=map(int,input().split())
for i in target_list:
    if i in num_list:
        print(1)
    else:
        print(0)
#이분 탐색 방법
n=int(input())
num_list=list(map(int, input().split()))
m=int(input())
target_list=list(map(int,input().split()))
num_list.sort()

for num in target_list:
    left,right=0,n-1
    flag=False

    while left<=right:
        mid=(left+right)//2
        if num==num_list[mid]:
            flag=True
            print(1)
            break
        elif num>num_list[mid]:
            left=mid+1
        else:
            right=mid-1
    if not flag:
        print(0)
