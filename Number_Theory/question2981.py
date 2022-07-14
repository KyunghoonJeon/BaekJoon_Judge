import sys
input=sys.stdin.readline
# N=int(input())
# num_list=[]
# for _ in range(N):
#     num_list.append(int(input()))
# num_list.sort()
# new_list=[]
# for i in range(1,N):
#     new_list.append(num_list[i]-num_list[0])

# def gcd_(a,b):
#     while b>0:
#         a,b=b,a%b
#     return a
# def gcd_N(arr):
#     gcd=arr[0]
#     for item in arr:
#         gcd=gcd_(gcd,item)
#     return gcd
# result=gcd_N(new_list)
# result_list=[]
# for j in range(1,int(result**(1/2))+1):
#     if result%j==0:
#         result_list.append(j)
#         if((j**2)!=result):
#             result_list.append(result//j)
# result_list.sort()
# del result_list[0]
# for _ in result_list:
#     print(_,end=' ')

#숏코딩
import math
t=int(input())
s=[]
a=[]
gcd=0
for i in range(t):
    s.append(int(input()))
    if i==1:
        gcd=abs(s[1]-s[0])
    gcd=math.gcd(abs(s[i]-s[i-1]),gcd)
gcd_a=int(gcd**1/2)
for i in range(2,gcd_a+1):
    if gcd%i==0:
        a.append(i)
        a.append(gcd//i)
a.append(gcd)
a=list(set(a))
a.sort()
for i in a:
    print(i,end=' ')