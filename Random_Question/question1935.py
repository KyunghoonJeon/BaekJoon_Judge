import sys
input=sys.stdin.readline
n=int(input())
s=input()
alpha=[0]*n
for i in range(n):
    alpha[i]=int(input())
stack=[]
for i in s:
    if 'A'<=i<='Z':
        stack.append(alpha[ord(i)-ord('A')])
    else:
        if i=='+':
            stack.append(stack.pop()+stack.pop())
        elif i=='-':
            stack.append(-(stack.pop()-stack.pop()))
        elif i=='*':
            stack.append(stack.pop()*stack.pop())
        elif i=='/':
            stack.append(1/(stack.pop()/stack.pop()))
print('%.2f'%stack[0])