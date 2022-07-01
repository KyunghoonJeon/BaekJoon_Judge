t=int(input())
for _ in range(t):
    b=input()
    for _ in range(len(b)//2):
        if '()' in b:
            b=b.replace('()','')
    if len(b)==0:
        print('YES')
    else:
        print('NO')