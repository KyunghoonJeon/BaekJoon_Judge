#Counting sort
# N=int(input())
# l=[]
# for i in range(N):
#     l.append(int(input()))

# def counting_sort(arr):
#     count=[0]*(max(arr)+1)
#     sorted_arr=list()

#     for i in arr:
#         count[i]+=1
    
#     for i in range(max(arr)+1):
#         for j in range(count[i]):
#             sorted_arr.append(i)
#     return sorted_arr

# for i in counting_sort(l):
#     print(i)
import sys
N=int(sys.stdin.readline())
b=[0]*10001
for i in range(N):
    b[int(sys.stdin.readline())]+=1
for i in range(10001):
    if b[i]!=0:
        for j in range(b[i]):
            print(i)