import sys
input=sys.stdin.readline
n=int(input())
graph=[list(map(int,input().rstrip())) for _ in range(n)]
def cut(x,y,n):
    check=graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=graph[i][j]:
                check=-1
                break
    if check==-1:
        print('(',end='')
        cut(x,y,n//2)
        cut(x,y+n//2,n//2)
        cut(x+n//2,y,n//2)
        cut(x+n//2,y+n//2,n//2)
        print(')',end='')
    elif check==1:
        print(1,end='')
    else:
        print(0,end='')
cut(0,0,n)