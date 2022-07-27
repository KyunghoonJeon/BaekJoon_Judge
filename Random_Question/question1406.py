import sys
input=sys.stdin.readline
st1=list(input().rstrip())
st2=[]
n=int(input())
for i in range(n):
    data=list(input().split())
    if data[0]=='P':
        st1.append(data[1])
    if data[0]=='L':
        if st1:
            st2.append(st1.pop())
    if data[0]=='D':
        if st2:
            st1.append(st2.pop())
    if data[0]=='B':
        if st1:
            st1.pop()
st2.reverse()
print(''.join(st1+st2))