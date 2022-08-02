#곱셈의 개수를 줄이는 분할 정복
import sys
input=sys.stdin.readline
A,B,C=map(int,input().split())
def power(a,b):
    if b==1:
        return a % C
    else:
        temp=power(a,b//2)
        if b%2==0:
            return temp*temp%C
        else:
            return temp*temp*a%C
print(power(A,B))