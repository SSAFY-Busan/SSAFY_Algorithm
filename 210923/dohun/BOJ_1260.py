from collections import deque

def DFS(V):
    visited[V] = True
    print(V, end=' ')

    for i in graph[V]:
        if not visited[i]:
           DFS(i)

def BFS(start):
    queue = deque([start])
    bfs_visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i] = True

# N은 정점의 개수, M은 간선의 개수, V는 시작 번호
N, M , V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
bfs_visited= [0] * (N+1)

# 양쪽으로 다 이동할 수 있기 때문에 2개를 추가해준다.
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은거 먼저 탐색하므로 정렬해주어야 한다.
for i in graph:
    i.sort()

DFS(V)
print()
BFS(V)

