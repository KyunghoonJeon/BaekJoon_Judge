import sys

K=int(input())
data=[int(sys.stdin.readline()) for i in range(K)]
s=[]
for i in data:
    if i!=0:
        s.append(i)
    if i==0:
        s.pop()
print(sum(s))