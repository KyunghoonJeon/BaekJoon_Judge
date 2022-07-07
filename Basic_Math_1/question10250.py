t=int(input())
for i in range(t):
    h,w,n=map(int,input().split())
    XX=(n//h)+1
    YY=n%h
    if n%h==0:
        XX=n//h
        YY=h
    print(f'{YY*100+XX}')