import sys
input=sys.stdin.readline
n=1000000
a = [False,False] + [True]*(n-1)
primes=[]
for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
primes=set(primes)
t=int(input())
for _ in range(t):
    n=int(input())
    a,b=n//2,n//2
    cnt=0
    while a>1:
        if a in primes and b in primes:
            a-=1;b+=1
            cnt+=1
        else:
            a-=1;b+=1
    print(cnt)