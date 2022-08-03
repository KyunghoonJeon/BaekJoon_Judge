import sys
input=sys.stdin.readline
n=int(input())
p=1000000007
A=[[1,1],[1,0]]
def mul(matrix1,matrix2):
    result=[[0 for _ in range(len(matrix2[1]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j]+=matrix1[i][k]*matrix2[k][j]
                result[i][j]%=p
    return result
def power(m,matrix):
    if m==1:
        return matrix
    else:
        temp=power(m//2,matrix)
        if m%2==0:
            return mul(temp,temp)
        else:
            return mul(mul(temp,temp),matrix)
if n<3:
    print(1)
else:
    ans=mul(power(n-2,A),[[1],[1]])
    print(ans[0][0])