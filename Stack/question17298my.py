import sys
N=int(input())
l=list(map(int,sys.stdin.readline().split()))
nge=[]
#for문이 두번이니까 당연히 시간초과 나겠지
for i in range(N):
    m=[]
    for j in range(i,N):
        if l[i]<l[j]:
            m.append(l[j])
    nge.append(m)
for i in nge:
    if len(i)==0:
        i.append(-1)
for i in range(N):
    print(nge[i][0], end=' ')