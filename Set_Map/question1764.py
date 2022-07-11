import sys
input=sys.stdin.readline
N,M=map(int, input().split())
s=set([input().rstrip() for _ in range(N)])
t=set([input().rstrip() for _ in range(M)])
l=sorted(list(s&t))
print(len(l))
for i in l:
    print(i)