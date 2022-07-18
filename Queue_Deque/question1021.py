import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
q=deque([])
for i in range(1,N+1):
    q.append(i)
num_list=list(map(int,input().split()))
cnt=0
for i in num_list:
    while True:
        if q[0]==i:
            q.popleft()
            break
        else:
            if q.index(i)<len(q)/2:
                while q[0]!=i:
                    q.append(q.popleft())
                    cnt+=1
            else:
                while q[0]!=i:
                    q.appendleft(q.pop())
                    cnt+=1
print(cnt)