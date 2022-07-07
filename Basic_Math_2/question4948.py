import math
#미리 소수의 집합을 정하자...!
num=[]
for i in range(2,246913):
    cnt=0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            cnt+=1
            break
    if cnt==0:
        num.append(i)
while True:
    n=int(input())
    a=0
    if n==0:
        break
    for i in num:
        if n<i<=2*n:
            a+=1
    print(a)