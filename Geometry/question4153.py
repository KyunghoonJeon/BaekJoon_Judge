import sys
input=sys.stdin.readline
# while True:
#     l=list(map(int, input().split()))
#     a=max(l)
#     if sum(l)==0:
#         break
#     l.remove(a)
#     if l[0]**2+l[1]**2==a**2:
#         print('right')
#     else:
#         print('wrong')
while True:
    a,b,c=sorted(map(int, input().split()))
    if a==0:break
    print('right' if a**2+b**2==c**2 else 'wrong')