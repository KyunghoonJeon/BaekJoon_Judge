import sys
input=sys.stdin.readline
n,k=map(int, input().split())
#아아아아아아아앙 two_count!!!
def two_count(n):
    cnt=0
    while n!=0:
        n//=2
        cnt+=n
    return cnt
def five_count(n):
    cnt=0
    while n!=0:
        n//=5
        cnt+=n
    return cnt
print(min(two_count(n)-two_count(k)-two_count(n-k),five_count(n)-five_count(k)-five_count(n-k)))