import sys
N=sys.stdin.readline()
l=[]
for i in N[:-1]:
    l.append(int(i))
l.sort(reverse=True)
for j in l:
    print(j,end='')