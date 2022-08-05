# t=int(input())
# for _ in range(t):
#     k=int(input())
#     file_list = [0]+list(map(int, input().split()))
#     dp=[[0 for i in range(k+1)] for i in range(k+1)] # 이중 리스트를 활용하여 빈칸 채우기
#     # 먼저 연속(2개)되어 있는 파일들의 합을 구한다
#     for j in range(1,k):
#         dp[j][j+1] = sum(file_list[j:j+2])


#     # 그 다음 단계(3개 연속되어있는 합 찾기)
#     for p in range(1,k-1):
#         dp[p][p+2] = min(dp[p][p]+dp[p+1][p+2], dp[p][p+1]+dp[p+2][p+2]) + sum(file_list[p:p+3])
#     # 그 다음 단계(4개 연속되어있는 합 찾기)
#     for q in range(1,k-2):
#         dp[q][q+3] = min(dp[q][q]+dp[q+1][q+3], dp[q][q+1]+dp[q+2][q+3], dp[q][q+2]+dp[q+3][q+3]) + sum(file_list[q:q+4])
# print(dp)

import sys
input=sys.stdin.readline
t=int(input().rstrip())
for _ in range(t):
    k=int(input().rstrip())
    file_list = [0]+list(map(int, input().rstrip().split()))
    dp=[[0 for __ in range(k+1)] for __ in range(k+1)]
    for r in range(1,k):
        dp[r][r+1] = sum(file_list[r:r+2])
    for i in range(1,k-1):
        for j in range(1,k-i):
            dp[j][j+i+1] = min([dp[j][j+h]+dp[j+h+1][j+i+1] for h in range(i+1)]) + sum(file_list[j:j+i+2])
    print(dp[1][k])
