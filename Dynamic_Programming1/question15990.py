import sys
input=sys.stdin.readline
dp = [[0 for _ in range(3)] for _ in range(100001)] #dp초기화
p=100000009
# 각각 1,2,3으로 끝나는 경우의 수
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]
for i in range(4, 100001):
    # 만약 i가 6일때

    # 5에서 2,3으로 끝난 경우들에 1을 더해주면 6이다.
    dp[i][0] =(dp[i - 1][1] + dp[i-1][2])%p
    # 4에서 1,3으로 끝난 경우들에 2를 더해주면 6이다.
    dp[i][1] = (dp[i - 2][0] + dp[i-2][2])%p
    # 3에서 1,2으로 경우 들에 3을 더해주면 6이다.
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1])%p
t=int(input())
for _ in range(t):
    n=int(input())
    print(sum(dp[n])%p)