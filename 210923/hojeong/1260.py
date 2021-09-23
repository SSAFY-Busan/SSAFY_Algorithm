# DFS와 BFS
def dfs(k):
    print(k, end=' ')
    visit[k] = 1  # 방문체크
    lst[k].sort()  # 정점 번호가 작은 것부터 방문
    for i in lst[k]:
        if visit[i] == 0:
            visit[i] = 1
            dfs(i)

def bfs(k):
    q = [k]
    visit[k] = 1  # 방문체크
    print(k, end=' ')
    while q:
        temp = q.pop(0)
        lst[temp].sort()
        for i in lst[temp]:
            if visit[i] == 0:
                visit[i] = 1
                print(i, end=' ')
                q.append(i)


N, M, V = map(int, input().split())  # N: 정점의 개수  M: 간선의 개수 V : 정점의 번호
lst = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)  # 방문체크
for i in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)  # 양방향
    lst[b].append(a)
dfs(V)
print()
visit = [0] * (N + 1)  # 초기화
bfs(V)
