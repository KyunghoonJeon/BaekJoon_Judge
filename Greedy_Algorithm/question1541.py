a=input().split('-')
num=[]
for i in a:
    sum=0
    b=i.split('+')
    for j in b:
        sum+=int(j)
    num.append(sum)
all=num[0]
for i in range(1,len(num)):
    all-=num[i]
print(all)