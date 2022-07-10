import sys
N=int(sys.stdin.readline())
dict=[]
for i in range(N):
    dict.append(sys.stdin.readline()[:-1])
dict=list(set(dict))
dict.sort()
dict.sort(key=len)
for i in dict:
    print(i)