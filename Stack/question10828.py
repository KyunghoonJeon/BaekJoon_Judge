import sys

class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self, val):
        self.items.append(val)
    
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return -1
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return -1

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        if self.__len__()==0:
            return 1
        else:
            return 0

N=int(input())
s=Stack()
l=[]
for i in range(N):
    data=list(sys.stdin.readline().split())
    if data[0]=='push':
        s.push(data[1])
    elif data[0]=='pop':
        l.append(s.pop())
    elif data[0]=='size':
        l.append(s.__len__())
    elif data[0]=='empty':
        l.append(s.isEmpty())
    elif data[0]=='top':
        l.append(s.top())
for i in l:
    print(i,end='\n')