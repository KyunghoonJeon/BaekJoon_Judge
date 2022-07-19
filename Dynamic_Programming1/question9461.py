import sys
input=sys.stdin.readline
def tri_dy(n):
    dp=[0]*(n+1)
    dp[1],dp[2],dp[3],dp[4],dp[5]=1,1,1,2,2
    for i in range(6,n+1):
        dp[i]=dp[i-1]+dp[i-5]
    return dp
p_n=tri_dy(100)
T=int(input())
for _ in range(T):
    N=int(input())
    print(p_n[N])