from string import ascii_lowercase
alphabet_list=list(ascii_lowercase)
add_alphabet=['c=','c-','dz=','d-','lj','nj','s=','z=']
n=input()
cnt=0
for i in add_alphabet:
    if i in n:
        n=n.replace(i,'1')
for j in alphabet_list:
    if j in n:
        n=n.replace(j,'1')
for k in n:
    cnt+=int(k)
print(cnt)