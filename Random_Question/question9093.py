import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    a=list(input().split())
    print(a)
    for j in a:
        print(j[::-1],end=' ')
