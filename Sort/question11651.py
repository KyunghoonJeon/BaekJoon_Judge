import sys
from operator import itemgetter
N=int(sys.stdin.readline())
l=[]
for i in range(N):
    l.append(list(map(int,sys.stdin.readline().split())))
l.sort(key=itemgetter(1,0))
for i in range(N):
    print(l[i][0],l[i][1])