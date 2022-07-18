import sys
from collections import deque
input=sys.stdin.readline
T=int(input())
for i in range(T):
    p=input()
    n=int(input())
    num_list=deque(input()[1:-2].split(','))
    flag=0
    if n==0:
        num_list=[]
    for j in p:
        if j=='R':
            flag+=1
        elif j=='D':
            if len(num_list)==0:
                print('error')
                break
            else:
                if flag%2==0:
                    num_list.popleft()
                else:
                    num_list.pop()
    else:
        if flag%2==0:
            print('['+','.join(num_list)+']')
        else:
            num_list.reverse()
            print('['+','.join(num_list)+']')