import sys
import math
input=sys.stdin.readline
N=int(input())
l=list(map(int,input().split()))
for i in range(N-1):
    a=math.gcd(l[0],l[i+1])
    x=int(l[0]/a)
    y=int(l[i+1]/a)
    print('{}/{}'.format(x,y))