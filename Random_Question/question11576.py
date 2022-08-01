import sys
input=sys.stdin.readline
a,b=map(int,input().split())
m=int(input())
l=list(map(int,input().split()))
l.reverse()
real=0
for i in range(m):
    real+=l[i]*(a**i)
res=[]
while real!=0:
    res.append(real%b)
    real//=b
print(' '.join(map(str,res[::-1])))