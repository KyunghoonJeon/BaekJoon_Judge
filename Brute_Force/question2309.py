dwarf=[]
for _ in range(9):
    dwarf.append(int(input()))
dwarf.sort()
total=sum(dwarf)
temp1,temp2=0,0
for i in range(9):
    for j in range(i+1,9):
        if 100==total-(dwarf[i]+dwarf[j]):
            temp1,temp2=dwarf[i],dwarf[j]
dwarf.remove(temp1)
dwarf.remove(temp2)
for i in dwarf:
    print(i)