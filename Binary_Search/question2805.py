import sys
input=sys.stdin.readline
n,m=map(int,input().split())
tree_list=list(map(int,input().split()))
start,end=1,max(tree_list)
while start<=end:
    mid=(start+end)//2
    get=0
    for i in tree_list:
        if i-mid>=0:
            get+=(i-mid)
    if get>=m:
        start=mid+1
    else:
        end=mid-1
print(end)