from re import L
import sys
input=sys.stdin.readline
n=int(input())
num_list=[]
ans_list=[]
flag=0
cnt=1
for i in range(n):
    num=int(input())
    while cnt<=num:
        num_list.append(cnt)
        ans_list.append('+')
        cnt+=1
    if num_list[-1]==num:
        num_list.pop()
        ans_list.append('-')
    else:
        print('NO')
        flag=1
        break
if flag==0:
    for i in ans_list:
        print(i)