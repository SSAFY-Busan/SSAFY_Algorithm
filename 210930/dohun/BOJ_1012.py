import sys
sys.setrecursionlimit(100000)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def DFS(x,y):
    # 방문처리
    visited[x][y] = 1
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위안에 들어오고 방문안했으면 방문
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and visited[nx][ny] == 0:
            DFS(nx,ny)

T = int(input())

for tc in range(T):
    # M은 가로길이, N은 세로길이, K는 배추개수
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for k in range(K):
        # a가 가로 b가 세로임
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == 0:
                DFS(i, j)
                cnt += 1

    print(cnt)