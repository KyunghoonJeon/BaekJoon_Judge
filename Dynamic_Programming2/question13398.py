import sys
input=sys.stdin.readline
n=int(input())
num_list=list(map(int,input().split()))
dp=[[0 for _ in range(n)] for _ in range(2)]
dp[0][0]=num_list[0];dp[1][0]=-1001
for i in range(1,n):
    # 예외없을때 연속합
    dp[0][i]=max(dp[0][i-1]+num_list[i], num_list[i])
    # 예외가 존재할때 연속합(두가지 경우가 존재)
    # 첫번째는 i번째를 제거할때
    # 두번째는 i번째 이전에 이미 하나를 제거했을때
    dp[1][i]=max(dp[0][i-1], dp[1][i-1]+num_list[i])
print(max(max(dp[0]),max(dp[1])))