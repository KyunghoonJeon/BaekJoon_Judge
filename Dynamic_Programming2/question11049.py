import sys
input=sys.stdin.readline
n=int(input().rstrip())
matrix_list=[[0,0]]
for _ in range(n):
    matrix_list.append(list(map(int,input().rstrip().split())))
dp=[[0 for __ in range(n+1)] for __ in range(n+1)]
for i in range(1, n):
    dp[i][i+1] = matrix_list[i][0]*matrix_list[i][1]*matrix_list[i+1][1]
for i in range(1,n-1):
    for j in range(1,n-i):
        dp[j][j+i+1] = min([dp[j][j+h]+dp[j+h+1][j+i+1]+matrix_list[j][0]*matrix_list[j+h][1]*matrix_list[j+i+1][1] for h in range(i+1)])
print(dp[1][n])