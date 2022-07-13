import sys
input=sys.stdin.readline
n,k=map(int, input().split())
mul1=1
for i in range(n,n-k,-1):
    mul1*=i
mul2=1
for j in range(1,k+1):
    mul2*=j
print(int(mul1/mul2))