bar=list(input())
cnt=0
stack=[]
for i in range(len(bar)):
    if bar[i]=='(':
        stack.append('(')
    else:
        if bar[i-1]=='(':
            stack.pop()
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1
print(cnt)