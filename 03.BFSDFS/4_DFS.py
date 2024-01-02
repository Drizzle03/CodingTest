
#그래프, 지금 방문 노드, 방문 리스트
def dfs(graph, v, visited):
    visited[v] = True #방문 처리
    print(v, end='') #출력
    for i in graph[v]: #현재 정점과 연결된 그래프 리스트 순회
        if not visited[i]: #만약 방문하지 않았다면
            dfs(graph, i, visited) #방문 

