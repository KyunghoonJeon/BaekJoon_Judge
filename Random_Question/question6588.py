import math
def prime(x):
    if x==1:
        return False
    elif x!=1:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return False
        return True
while True:
    flag=True
    n=int(input())
    if n==0: break
    for i in range(3,n+1,2):
        if prime(i):
            if prime(n-i):
                print(f'{n} = {i} + {n-i}')
                flag=False
                break
    if flag:
        print("Goldbach's congecture is wrong.")