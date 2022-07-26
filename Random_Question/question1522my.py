import sys
l = list(sys.stdin.readline())
l=l[:-1]
cnt_a=l.count('a')
cnt_b=l.count('b')
com=[]
for i in range(cnt_a+1):
    new=[]
    for j in range(i):
        new.append('a')
    for k in range(cnt_b):
        new.append('b')
    for f in range(cnt_a-i):
        new.append('a')
    com.append(new)
for i in range(cnt_b+1):
    new2=[]
    for j in range(i):
        new2.append('b')
    for k in range(cnt_a):
        new2.append('a')
    for f in range(cnt_a-i):
        new2.append('b')
    com.append(new2)
move=[]
for i in com:
    cnt=0
    for j in range(cnt_a+cnt_b):
        if l[j]!=i[j]:
            cnt+=1
        else:
            cnt+=0
    move.append(cnt)
print(int(min(move)/2))