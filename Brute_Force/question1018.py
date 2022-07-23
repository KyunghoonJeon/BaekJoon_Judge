import sys
input=sys.stdin.readline
n,m=map(int,input().split())
chess=[]
cnt=[]
for i in range(n):
    chess.append(input())
#시작점 잡아주기
for a in range(n-7):
    for b in range(m-7):
        start_w=0
        start_b=0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2==0:
                    if chess[i][j]!='W':
                        start_w+=1
                    if chess[i][j]!='B':
                        start_b+=1
                else:
                    if chess[i][j]!='B':
                        start_w+=1
                    if chess[i][j]!='W':
                        start_b+=1
        cnt.append(start_w);cnt.append(start_b)
print(min(cnt))