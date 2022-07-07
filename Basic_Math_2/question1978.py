N=int(input())
l=list(map(int, input().split()))
prime_list=[]
def prime(x):
    if x==1:
        return False
    elif x!=1:
        for i in range(2,x):
            if x%i==0:
                return False
        return True
for i in l:
    prime_list.append(prime(i))
print(prime_list.count(True))
