import sys
sys.setrecursionlimit(10**5) # 재귀 호출과 관련이 깊다. 스택 깊이 제한을 푸는 메서드
input=sys.stdin.readline

def dfs(graph, v, visited):
    global order
    visited[v]=True
    traversal_order[v]=order
    order+=1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


n,m,r=map(int, input().split())
# 그래프를 array형태로 만드는 과정(정렬을 한 이유는 오름차순으로 경로를 만들기 때문에)
graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph:
    g.sort(reverse=True)

visited=[False]*(n+1)
traversal_order=[0]*(n+1)
order=1

dfs(graph, r, visited)
for i in range(1,len(traversal_order)):
    print(traversal_order[i])