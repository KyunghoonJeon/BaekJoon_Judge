import sys
from collections import Counter
input=sys.stdin.readline
n=int(input())
num_list=list(map(int,input().split()))
c=Counter(num_list)
result=[-1 for _ in range(n)]
stack=[0]
for i in range(1,n):
    while stack and c[num_list[stack[-1]]]<c[num_list[i]]:
        result[stack.pop()]=num_list[i]
    stack.append(i)
print(*result)