n,m=map(int, input().split())
c=list(map(int,input().split()))

result=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if c[i]+c[j]+c[k] > m:
                continue
            else:
                result=max(result,c[i]+c[j]+c[k])

print(result)
