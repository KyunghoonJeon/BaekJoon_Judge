import sys
from collections import Counter
N=int(sys.stdin.readline())
l=[]
for i in range(N):
    l.append(int(sys.stdin.readline()))
l.sort()
print(round(sum(l)/N))
print(l[N//2])
#최빈값
cnt=Counter(l)
mode=cnt.most_common(2)
if mode[0][1]==mode[1][1]:
    print(mode[0][1])
else:
    print(mode[0][0])
print(l[-1]-l[0])