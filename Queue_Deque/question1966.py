import sys
from collections import deque
input=sys.stdin.readline
S=int(input())
for i in range(S):
    N,M=map(int,input().split())
    num_list=deque(list(map(int,input().split())))
    idx_list=deque(list(range(N)))
    cnt=0
    while num_list:
        if num_list[0]==max(num_list):
            cnt+=1
            num_list.popleft()
            if idx_list.popleft()==M:
                print(cnt)
        else:
            num_list.append(num_list.popleft())
            idx_list.append(idx_list.popleft())
            