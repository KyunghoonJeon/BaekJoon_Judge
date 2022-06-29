N=int(input())
l=list(map(int, input().split()))
l.sort()
result=0
for i in range(N):
    result+=(N-i)*l[i]
print(result)