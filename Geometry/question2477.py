import sys
input=sys.stdin.readline
N=int(input())
l=[]
for i in range(6):
    l.append(list(map(int, input().split())))
w=0;w_idx=0
h=0;h_idx=0
for i in range(6):
    if l[i][0]==1 or l[i][0]==2:
        if w<l[i][1]:
            w=l[i][1]
            w_idx=i
    if l[i][0]==3 or l[i][0]==4:
        if h<l[i][1]:
            h=l[i][1]
            h_idx=i
box_w=l[(h_idx+3)%6][1]
box_h=l[(w_idx+3)%6][1]
area=w*h-box_w*box_h
print(area*N)