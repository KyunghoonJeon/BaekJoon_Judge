import sys
input=sys.stdin.readline
n,c=map(int,input().split())
house=[]
for _ in range(n):
    house.append(int(input()))
house.sort()
start,end=1,house[-1]-house[0]
while start<=end:
    mid=(start+end)//2
    cnt=1
    curr=house[0]
    for i in range(1,n):
        if house[i]-curr>=mid:
            cnt+=1
            curr=house[i]
    if cnt>=c:
        start=mid+1
    else:
        end=mid-1
print(mid)