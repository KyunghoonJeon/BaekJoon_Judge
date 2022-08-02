import sys
input=sys.stdin.readline
N,K=map(int,input().split())
p=1000000007
def fac(c):
    n=1
    for i in range(2,c+1):
        n=(n*i)%p
    return n
def power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a % p
    else:
        temp=power(a,b//2)
        if b%2==0:
            return temp*temp%p
        else:
            return temp*temp*a%p

top=fac(N);bot=fac(N-K)*fac(K)
print(top*power(bot,p-2)%p)