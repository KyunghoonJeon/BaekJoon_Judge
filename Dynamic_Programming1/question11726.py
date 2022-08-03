import sys
input=sys.stdin.readline
n=int(input())
np=[0,1,2]
for i in range(3,1001):
    np.append(np[i-2]+np[i-1])
print(np[n])