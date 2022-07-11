import sys
N,M=map(int,sys.stdin.readline().split())
dict1=[]
dict2=[]
for i in range(N):
    dict1.append(sys.stdin.readline())
for i in range(M):
    dict2.append(sys.stdin.readline())
dict1=set(dict1)
cnt=0
for i in dict2:
    if i in dict1:
        cnt+=1
print(cnt)