n=int(input())
data=[]
rank=[0 for _ in range(n)]
#cnt를 전역변수로 쓰면 안되는구나.

for i in range(n):
    a,b=map(int, input().split())
    data.append((a,b))
for i in range(n):
    cnt=0
    for j in range(n):
        if data[i][0]<data[j][0] and data[i][1]<data[j][1]:
            cnt+=1
    rank.append(cnt+1)

for i in rank:
    print(i,end=" ")