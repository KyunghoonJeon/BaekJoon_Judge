import sys
input=sys.stdin.readline
# N=int(input())
# cnt=0
# for i in range(1,N+1):
#     if i%5==0:
#         cnt+=1
#         if i%25==0:
#             cnt+=1
#             if i%125==0:
#                 cnt+=1
# print(cnt)
N=int(input())
def five_count(n):
    cnt=0
    while n!=0:
        n//=5
        cnt+=n
    return cnt
print(five_count(N))