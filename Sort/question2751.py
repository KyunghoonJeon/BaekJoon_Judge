import sys
N=int(sys.stdin.readline())
l=[]
for i in range(N):
    l.append(int(sys.stdin.readline()))
for j in sorted(l):
    print(j)