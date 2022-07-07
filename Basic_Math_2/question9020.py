import math
def prime(x):
    if x==1:
        return False
    elif x!=1:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return False
        return True
#가운데서부터 비교한다. 왜냐? 차이가 작은 값이 답이니까
T=int(input())
for i in range(T):
    n=int(input())
    a,b=n//2,n//2
    while a>0:
        if prime(a) and prime(b):
            print(a,b)
            break
        else:
            a-=1
            b+=1