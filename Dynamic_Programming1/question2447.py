import sys
input=sys.stdin.readline
def star(l):
    if l==3:
        return ['***','* *','***']
    new=star(l//3)
    stars=[]
    for i in new:
        stars.append(i*3)
    for i in new:
        stars.append(i+' '*(l//3)+i)
    for i in new:
        stars.append(i*3)
    return stars
n=int(input())
print('\n'.join(star(n)))