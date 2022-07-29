import sys
from math import gcd
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    s=len(l)
    m=[]
    for i in range(1,s):
        for j in range(i+1,s):
            m.append(gcd(l[i],l[j]))
    print(sum(m))