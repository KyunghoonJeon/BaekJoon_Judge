import sys
from math import gcd
input=sys.stdin.readline
n,s=map(int,input().split())
l=list(map(int,input().split()))
dif=list(set(abs(l[i]-s) for i in range(n)))
res=min(dif)
for j in range(len(dif)):
    res=gcd(dif[j],res)
print(res)