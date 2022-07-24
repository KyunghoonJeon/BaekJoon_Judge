import sys
import bisect
input=sys.stdin.readline
n=int(input())
num_list=list(map(int,input().split()))
m=int(input())
target_list=list(map(int,input().split()))
num_list.sort()

# 이미 존재하는 매서드 활용
# for num in target_list:
#     first=bisect.bisect_left(num_list,num)
#     second=bisect.bisect_right(num_list,num)
#     print(second-first,end=' ')

def bs(l,target,start,end):
    if start>end:
        return 0
    mid=(start+end)//2
    if l[mid]==target:
        return cnt.get(target)
    elif l[mid]>target:
        return bs(l,target,start,mid-1)
    else:
        return bs(l,target,mid+1,end)
cnt={}
for i in num_list:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1
for i in target_list:
    print(bs(num_list,i,0,n-1),end=' ')