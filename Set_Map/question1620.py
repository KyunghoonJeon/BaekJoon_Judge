import sys
N,M=map(int, sys.stdin.readline().split())
s=list([sys.stdin.readline().rstrip() for _ in range(N)])
t=list([sys.stdin.readline().rstrip() for _ in range(M)])
dic={s[i]:i+1 for i in range(N)}
for i in t:
    if i.isdigit(): #문자열이 숫자로만 이루어져있는지 아닌지
        print(s[int(i)-1])
    else:
        print(dic[i])