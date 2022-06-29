N=int(input())
ways=list(map(int,input().split()))
city=list(map(int,input().split()))
min_city=city[0]
sum=0
for i in range(N-1):
    if min_city>city[i]:
        min_city=city[i]
    sum+=min_city*ways[i]
print(sum)