# 유기농 배추
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    visited[r][c] = 1
    q = deque([[r, c]])
    while q:
        t = q.popleft()
        for d in range(4):
            nr = t[0] + dr[d]
            nc = t[1] + dc[d]
            if 0 <= nr < N and 0 <= nc < M and ground[nr][nc] == 1 and (visited[nr][nc] == 0):
                visited[nr][nc] = 1
                q.append([nr, nc])


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for i in range(K):
        c, r = map(int, input().split())
        ground[r][c] = 1

    cnt = 0
    for r in range(N):
        for c in range(M):
            if ground[r][c] == 1 and (visited[r][c] == 0):
                bfs(r, c)
                cnt += 1
    print(cnt)
