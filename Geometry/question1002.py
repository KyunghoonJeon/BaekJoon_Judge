import sys
import math 
input=sys.stdin.readline
T=int(input())
for i in range(T):
    l=list(map(int, input().split()))
    dis=math.sqrt((l[0]-l[3])**2+(l[1]-l[4])**2)
    if dis==0 and l[2]==l[5]:
        print(-1)
    elif abs(l[2]-l[5])==dis or l[2]+l[5]==dis:
        print(1)
    elif abs(l[2]-l[5])<dis<l[2]+l[5]:
        print(2)
    else:
        print(0)