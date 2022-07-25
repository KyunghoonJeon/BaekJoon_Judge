# import sys
# input=sys.stdin.readline
# n=int(input())
# num_list=list(map(int,input().split()))
# arr=[0]
# for i in range(n):
#     start,end=0,len(arr)-1
#     while start<=end:
#         mid=(start+end)//2
#         if arr[mid]<num_list[i]:
#             start=mid+1
#         else:
#             end=mid-1
#     if start>=len(arr):
#         arr.append(num_list[i])
#     else:
#         arr[start]=num_list[i]
# print(len(arr)-1)

import sys
input = sys.stdin.readline

n = int(input())
cases = list(map(int, input().split()))
lis = [0]

for case in cases:
    if lis[-1]<case:
        lis.append(case)
    else:
        left = 0
        right = len(lis)

        while left<right:
            mid = (right+left)//2
            if lis[mid]<case:
                left = mid+1
            else:
                right = mid
        lis[right] = case

print(len(lis)-1)