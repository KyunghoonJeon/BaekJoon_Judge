import sys
input=sys.stdin.readline
n,b=map(int,input().split())
p=1000
A=[]
for _ in range(n):
    A.append(list(map(int,input().split())))
def mul(matrix1,matrix2,n):
    result=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j]+=matrix1[i][k]*matrix2[k][j]
                result[i][j]%=1000
    return result
def power(n,b,matrix):
    if b==1:
        return matrix
    else:
        temp=power(n,b//2,matrix)
        if b%2==0:
            return mul(temp,temp,n)
        else:
            return mul(mul(temp,temp,n),matrix,n)
ans=power(n,b,A)
for i in ans:
    for j in i:
        print(j%p,end=' ')
    print()