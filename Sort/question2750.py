#Bubble sort
N=int(input())
l=[]
for i in range(N):
    l.append(int(input()))

# for i in range(len(l)-1,0,-1):
#     for j in range(i):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# for i in l:
#     print(i)

#Insertion sort
for i in range(1,len(l)):
    j=i
    while j>0 and l[j-1]>l[j]:
        l[j-1],l[j]=l[j],l[j-1]
        j-=1
for i in l:
    print(i)
