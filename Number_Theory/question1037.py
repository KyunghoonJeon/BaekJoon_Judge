import sys
input=sys.stdin.readline
N=int(input())
l=list(map(int, input().split()))
if len(l)==1:
    print(l[0]**2)
else:
    print(max(l)*min(l))