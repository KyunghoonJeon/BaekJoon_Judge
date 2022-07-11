import sys
input=sys.stdin.readline
N=int(input())
s=list(map(int, input().split()))
M=int(input())
t=list(map(int, input().split()))
count={}
for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i in t:
    if i in count:
        print(count[i],end=' ')
    else:
        print(0,end=' ')
print(count)