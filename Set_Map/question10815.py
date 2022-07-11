#리스트는 인덱스 0부터 n까지 일일이 검사를 해야하므로 
# 시간복잡도가 O(n) 이고, set은 O(1)이라고 한다.
import sys
N=int(sys.stdin.readline())
num_list=set(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
new_list=list(map(int,sys.stdin.readline().split()))
for i in range(M):
    if new_list[i] in num_list:
        print(1,end=' ')
    else:
        print(0,end=' ')
