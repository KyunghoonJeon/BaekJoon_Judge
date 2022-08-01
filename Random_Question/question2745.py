# a,b=input().rstrip().split()
# print(int(a,int(b)))

# import sys
# input=sys.stdin.readline
# system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# n,b=map(int,input().split())
# s=''
# while n:
#     s+=str(system[n%b])
#     n//=b
# print(s[::-1])

import sys
input=sys.stdin.readline
system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n,b=input().split()
result=0
n=''.join(reversed(n));b=int(b)
for i in range(len(n)-1,-1,-1):
    sum=system.index(n[i])*(b**i)
    result+=sum
print(result)