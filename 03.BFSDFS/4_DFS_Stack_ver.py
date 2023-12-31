def dfs(graph, v, visited):
    visited[v] = True #방문 처리
    print(v, end=' ') #출력

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: #현재 노드와 연결된 타노드들 방문
        if not visited[i]: #방문 처리가 안 되어있으면
            dfs(graph, i, visited) #또 재귀적으로 들어감

# 그래프 입력
graph = [
    [], 
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
dfs(graph, 1, visited)