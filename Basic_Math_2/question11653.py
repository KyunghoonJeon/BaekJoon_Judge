def factorization(x):
    d=2
    while d<=x:
        if x==0:
            print()
        elif x%d==0:
            print(d)
            x=x/d
        else:
            d=d+1
factorization(int(input()))