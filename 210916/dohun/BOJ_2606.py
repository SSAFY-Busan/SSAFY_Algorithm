# def DFS(v):
#     visited[v] = 1
#     for i in graph[v]:
#         if not visited[i]:
#             DFS(i)

from collections import deque
def BFS():
    q = deque()
    q.append(1)
    while q:
        number = q.popleft()
        for i in graph[number]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)


com = int(input()) # 컴퓨터 수

N = int(input())
graph = [[] for _ in range(com+1)]
visited = [0] * (com+1)

for i in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS(1)
BFS()

print(sum(visited)-1)