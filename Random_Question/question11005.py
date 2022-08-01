import sys
input=sys.stdin.readline
system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n,b=map(int,input().split())
s=''
while n:
    s+=str(system[n%b])
    n//=b
print(s[::-1])