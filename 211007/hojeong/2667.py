# 단지번호붙이기
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    size = 1
    q = deque([[r, c]])
    visited[r][c] = 1
    while q:
        t = q.popleft()
        for d in range(4):
            nr = t[0] + dr[d]
            nc = t[1] + dc[d]
            if 0 <= nr < N and 0 <= nc < N and homes[nr][nc] == 1 and (visited[nr][nc] == 0):
                visited[nr][nc] = 1
                size += 1
                q.append([nr, nc])
    sizes.append(size)


N = int(input())
homes = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

sizes = []
for r in range(N):
    for c in range(N):
        if homes[r][c] == 1 and visited[r][c] == 0:
            bfs(r, c)

sizes.sort()  # 오름차순 출력해야함
print(len(sizes))
for i in sizes:
    print(i)
