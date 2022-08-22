import sys
input=sys.stdin.readline
n=int(input())
data=input()

res=0
for i in range(n):
    res+=(ord(data[i])-96)*(31**i)%1234567981
print(res%1234567891)