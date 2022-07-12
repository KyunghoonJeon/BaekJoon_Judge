import sys
input=sys.stdin.readline
a,b=map(int, input().split())
A=set(map(int, input().split()))
B=set(map(int, input().split()))
C=(A | B)-(A & B)
print(len(C))