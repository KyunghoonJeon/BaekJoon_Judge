import sys
input=sys.stdin.readline
N=int(input())
# def fib_rec(n):
#     cnt1=0
#     if n==1 or n==2:
#         return 1
#     else:
#         return fib_rec(n-1)+fib_rec(n-2)
def fib_rec(n):
    dp=[0]*(n+1)
    cnt=0
    dp[1],dp[2]=1,1
    for i in range(3,n+1):
        cnt+=1
        dp[i]=dp[i-1]+dp[i-2]
    return cnt

def fib_dy(n):
    dp=[0]*(n+1)
    dp[1],dp[2]=1,1
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[i]
print(fib_dy(N),fib_rec(N))
