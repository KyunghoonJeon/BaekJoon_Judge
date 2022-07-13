import sys
input=sys.stdin.readline
T=int(input())
# for i in range(T):
#     A,B=map(int, input().split())
#     for j in range(max(A,B),(A*B)+1):
#         if j%A==0 and j%B==0:
#             print(j)
#             break

#유클리드 접근법
for i in range(T):
    a,b=map(int, input().split())
    A,B=a,b
    while a!=0:
        b=b%a
        a,b=b,a
    gcd=b
    lcm=A*B//b
    print(lcm)