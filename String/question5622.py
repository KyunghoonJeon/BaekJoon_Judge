l=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word_number=[]
word=input()
for i in range(len(l)):
    for j in word:
        if j in l[i]:
            word_number.append(i+3)
print(sum(word_number))
