import sys
N=int(sys.stdin.readline())
# l=[]
# for i in range(10000000):
#     if '666' in str(i):
#         l.append(i)
# print(l[N-1])

cnt=0
six_n=666
while True:
    if '666' in str(six_n):
        cnt+=1
    if cnt==N:
        print(six_n)
        break
    six_n+=1