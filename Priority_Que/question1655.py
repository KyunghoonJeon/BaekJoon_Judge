import sys
import heapq
input=sys.stdin.readline
n=int(input())
l_heap=[];r_heap=[] #l_heap은 최대힙, r_heap는 최소힙
mid=int(input())
print(mid)
for _ in range(1,n):
    a=int(input())
    if a>mid:
        heapq.heappush(r_heap,a)
        if len(l_heap)+1<len(r_heap):
            heapq.heappush(l_heap,(-mid,mid))
            mid=heapq.heappop(r_heap)
    else:
        heapq.heappush(l_heap,(-a,a))
        if len(r_heap)<len(l_heap):
            heapq.heappush(r_heap,mid)
            mid=heapq.heappop(l_heap)[1]
    print(mid)