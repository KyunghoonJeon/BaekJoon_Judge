a,b,c=map(int, input().split())
#연산을 최소화.....뺄셈보다는 비교가 낫다
if b>=c:
    print(-1)
else:
    print(int(a/(c-b))+1)
