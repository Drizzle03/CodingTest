from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    print(start, end=' ')

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True