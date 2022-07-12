import sys
input=sys.stdin.readline
S=input()
l=[]
for i in range(len(S)):
    for j in range(i+1,len(S)):
        l.append(S[i:j])
l=list(set(l))
print(len(l))