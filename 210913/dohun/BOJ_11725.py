import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input()) # 노드 개수
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(N+1)]

def DFS(start, graph, visited):
    for i in graph[start]:
        # 방문 안한거면 start가 부모
        if visited[i] == 0:
            visited[i] = start
            DFS(i, graph, visited)

DFS(1, graph, visited)

for i in range(2, N+1):
    print(visited[i])
