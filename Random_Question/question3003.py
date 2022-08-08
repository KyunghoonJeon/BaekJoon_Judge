real=[1,1,2,2,2,8]
curr=list(map(int,input().split()))
l=[]
for i in range(len(real)):
    l.append(real[i]-curr[i])
print(*l)