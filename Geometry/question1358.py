import sys
import math
input=sys.stdin.readline
w,h,x,y,p=map(int,input().split())
cnt=0
for i in range(p):
    a,b=map(int,input().split())
    dis1=math.sqrt((a-x)**2+(b-(y+h/2))**2)
    dis2=math.sqrt((a-(x+w))**2+(b-(y+h/2))**2)
    if dis1<=(h/2) or dis2<=(h/2) or (x<=a<=x+w and y<=b<=y+h):
        cnt+=1
print(cnt)