s=input()
switch=[]
answer=[]
flag=0
for i in range(len(s)):
    if flag==0:
        if s[i]=='<'or s[i]==' ':
            if s[i]=='<':
                flag=1
            answer+=switch[::-1]
            switch=[]
            answer+=s[i]
        else:
            switch.append(s[i])
    elif flag==1:
        if s[i]=='>':
            flag=0
        answer.append(s[i])
if switch:
    answer+=switch[::-1]
for i in range(len(answer)):
    print(answer[i],end='')