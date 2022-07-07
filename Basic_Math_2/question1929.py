import math
M,N=map(int,input().split())
l=[]
def prime(x):
    if x==1:
        return False
    elif x!=1:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return False
        return True
for i in range(M,N+1):
    if prime(i):
        print(i)