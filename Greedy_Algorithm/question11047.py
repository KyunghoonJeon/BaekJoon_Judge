N,K=map(int, input().split())
coin=[]
num=0
for i in range(N):
    coin.append(int(input()))
coin.reverse()
for i in coin:
    if K//i==0:
        continue
    else:
        num+=K//i
        K-=(K//i)*i
print(num)