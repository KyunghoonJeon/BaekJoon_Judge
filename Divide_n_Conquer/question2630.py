import sys
input=sys.stdin.readline
n=int(input())
paper=[[0]*n for i in range(n)]
for i in range(n):
    paper[i]=list(map(int,input().split()))
w_cnt=0;b_cnt=0
def cut(x,y,n):
    global w_cnt,b_cnt
    check=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=paper[i][j]:
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return
    if check==0:
        w_cnt+=1
        return
    else:
        b_cnt+=1
        return 
cut(0,0,n)
print(w_cnt)
print(b_cnt)
