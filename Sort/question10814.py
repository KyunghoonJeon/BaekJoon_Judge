import sys
N=int(sys.stdin.readline())
l=[]
for i in range(N):
    l.append(sys.stdin.readline().split())
l.sort(key=lambda x: int(x[0]))
for i in range(N):
    print(l[i][0],l[i][1])