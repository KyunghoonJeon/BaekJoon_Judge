import sys
input=sys.stdin.readline
n=int(input())
df=[]
for _ in range(n):
    df.append(list(map(int,input().split())))
for i in range(1,n):
    for j in range(len(df[i])):
        if j==0:
            df[i][j]=df[i][j]+df[i-1][j]
        elif j==len(df[i])-1:
            df[i][j]=df[i][j]+df[i-1][j-1]
        else:
            df[i][j]=df[i][j]+max(df[i-1][j-1],df[i-1][j])
print(max(df[n-1]))