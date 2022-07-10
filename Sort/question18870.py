import sys
N=int(sys.stdin.readline())
X=list(map(int,sys.stdin.readline().split()))
new=sorted(list(set(X)))
dic={new[i]:i for i in range(len(new))}
for i in X:
    print(dic[i],end=' ')