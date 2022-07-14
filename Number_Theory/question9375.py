import sys
from collections import Counter
input=sys.stdin.readline
T=int(input())
for i in range(T):
    N=int(input())
    l=[]
    for j in range(N):
        a,b=input().split()
        l.append(b)
    cnt=1
    check=Counter(l)
    for key in check:
        cnt*=check[key]+1
    print(cnt-1)