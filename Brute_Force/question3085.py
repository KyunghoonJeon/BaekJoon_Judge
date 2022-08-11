import sys
input=sys.stdin.readline

n=int(input())

candy=[]
for _ in range(n):
    candy.append(list(map(str,input())))

maxcnt=0

# 배열의 행 마다 같은 색의 사탕이 몇개 있는지 계산
def width(): 
    global maxcnt
    for k in range(n):
        countRow=1 # 초기 개수를 1로 초기화
        for l in range(n-1):
            if candy[k][l]==candy[k][l+1]:
                countRow+=1
                maxcnt=max(maxcnt,countRow)
            else:
                countRow=1

def height():
    for k in range(n):
        global maxcnt
        countCol=1 # 초기 개수를 1로 초기화
        for l in range(n-1):
            if candy[l][k]==candy[l+1][k]:
                countCol+=1
                maxcnt=max(maxcnt,countCol)
            else:
                countCol=1

for i in range(n):
    for j in range(n-1):
        # 입력 받은 배열의 행의 원소가 다르다면
        if candy[i][j]!=candy[i][j+1]:
            candy[i][j],candy[i][j+1]=candy[i][j+1],candy[i][j]
            width()
            height()
            candy[i][j+1],candy[i][j]=candy[i][j],candy[i][j+1]
        # 입력 받은 배열의 열의 원소가 다르다면
        if candy[j][i]!=candy[j+1][i]:
            candy[j][i],candy[j+1][i]=candy[j+1][i],candy[j][i]
            width()
            height()
            candy[j+1][i],candy[j][i]=candy[j][i],candy[j+1][i]
print(maxcnt)