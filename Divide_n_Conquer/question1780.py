import sys
input=sys.stdin.readline
n=int(input())
paper=[list(map(int,input().rstrip().split())) for _ in range(n)]
f_cnt=0;s_cnt=0;t_cnt=0
def cut(x,y,n):
    global f_cnt,s_cnt,t_cnt
    check=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        cut(x+k*n//3,y+l*n//3,n//3)
                return
    if check==-1:
        f_cnt+=1
    elif check==0:
        s_cnt+=1
    else:
        t_cnt+=1
cut(0,0,n)
print(f_cnt);print(s_cnt);print(t_cnt)