import sys
input=sys.stdin.readline
T=int(input())
for i in range(T):
    n,m=map(int, input().split())
    mul1=1
    for i in range(m,m-n,-1):
        mul1*=i
    mul2=1
    for j in range(1,n+1):
        mul2*=j
    val=int(mul1//mul2)
    print(val)