M=int(input())
N=int(input())
l=[]
def prime(x):
    if x==1:
        return False
    elif x!=1:
        for i in range(2,x):
            if x%i==0:
                return False
        return True
for i in range(M,N+1):
    if prime(i)==True:
        l.append(i)
if len(l)==0:
    print(-1)
else:
    print(sum(l))
    print(l[-1])