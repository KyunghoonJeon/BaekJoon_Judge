import sys
input=sys.stdin.readline
n=int(input().rstrip())
num_list=list(map(int,input().rstrip().split()))
dp=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    dp[i][i]=1
for i in range(n-1):
    if num_list[i] == num_list[i+1]:
        dp[i][i+1]=1
# dp를 채울때 대각선으로 채워라
# for i in range(n-2):
#     j=i+2
#     if num_list[i] == num_list[j] and dp[i+1][j-1] == 1:
#         dp[i][j]=1
# for i in range(n-3):
#     j=i+3
#     if num_list[i] == num_list[j] and dp[i+1][j-1] == 1:
#         dp[i][j]=1
# for i in range(n-4):
#     j=i+4
#     if num_list[i] == num_list[j] and dp[i+1][j-1] == 1:
#         dp[i][j]=1
# for i in range(n-5):
#     j=i+5
#     if num_list[i] == num_list[j] and dp[i+1][j-1] == 1:
#         dp[i][j]=1
# for i in range(n-6):
#     j=i+6
#     if num_list[i] == num_list[j] and dp[i+1][j-1] == 1:
#         dp[i][j]=1
for k in range(2,n):
    for i in range(n-k):
        j=i+k
        if num_list[i] == num_list[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1
m=int(input().rstrip())
for _ in range(m):
    s,e=map(int,input().rstrip().split())
    print(dp[s-1][e-1])