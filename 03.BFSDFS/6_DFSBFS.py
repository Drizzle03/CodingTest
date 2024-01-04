from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    visited[v] = True
    queue = deque([v])

    while queue:
        t = queue.popleft()
        print(t, end=' ')

        for i in graph[t]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

n, m, v = map(int, input().split())

graph = [ [] for _ in range (n+1)]
visited = [ False for _ in range (n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

dfs(v)
visited = [ False for _ in range (n+1)]
print()
bfs(v)