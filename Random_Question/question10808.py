from string import ascii_lowercase
s=input()
alpha_list=list(ascii_lowercase)
cnt=[]
for i in alpha_list:
    cnt.append(s.count(i))
print(*cnt)