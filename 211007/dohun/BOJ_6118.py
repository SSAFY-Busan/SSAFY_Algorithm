from collections import deque

def BFS(V):
    queue = deque()
    queue.append(V)
    visited[V] = 1
    while queue:
        new_V = queue.popleft()
        for i in graph[new_V]:
            if visited[i] == 0:
                visited[i] = visited[new_V] + 1
                queue.append(i)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

BFS(1)

# 가장 먼저 있는 최대값 위치 가져오기
print(visited.index(max(visited)), end=' ')

# 1과 최대값 위치의 거리 가져오기 1부터 시작하여 -1 필요
print(visited[visited.index(max(visited))]-1, end=' ')
print(visited.count(max(visited)))