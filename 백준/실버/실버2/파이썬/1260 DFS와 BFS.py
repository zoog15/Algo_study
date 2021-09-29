# 1260번 DFS와 BFS : https://www.acmicpc.net/problem/1260
from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())  # n: 정점의 개수, m: 간선의 개수, v: 탐색 시작할 정점의 번호
graph = [[] for _ in range(n+1)]
graph[0] = [0,0]
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()

visited = [False for _ in range(n+1)]
dfs(graph,v,visited)

print()

visited = [False for _ in range(n+1)]
bfs(graph,v,visited)