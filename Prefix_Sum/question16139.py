import sys
import string
input=sys.stdin.readline
s=input()
t=int(input())
char_dic = {}
for char in string.ascii_lowercase:
    char_dic[char] = [0]
    count = 0
    for i in range(len(s)):
        if s[i] == char:
            count += 1
        char_dic[char].append(count)
for _ in range(t):
    char,s,e=input().split()
    s=int(s);e=int(e)
    print(char_dic[char][e+1]-char_dic[char][s])