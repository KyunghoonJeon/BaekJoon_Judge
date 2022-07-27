from re import L
import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
q=deque([])
for i in range(n):
    data=list(input().split())
    if data[0]=='push':
        q.append(data[1])
    if data[0]=='pop':
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
    if data[0]=='size':
        print(len(q))
    if data[0]=='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    if data[0]=='front':
        print(q[0])
    if data[0]=='back':
        print(q[-1])
