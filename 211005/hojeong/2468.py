# 안전영역
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    while q:
        t = q.popleft()
        for d in range(4):
            nr = t[0] + dr[d]
            nc = t[1] + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and flood[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc))


# 침수 체크하기
def check(h):
    for r in range(N):
        for c in range(N):
            if space[r][c] <= h:
                flood[r][c] = 1


N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

# 최대 높이 구하기
MAX = 0
for r in range(N):
    temp = max(space[r])
    if MAX < temp:
        MAX = temp

# 0부터 MAX까지 안전영역 구해서 값 갱신
safe = 0
for h in range(MAX + 1):
    visited = [[0] * N for _ in range(N)]
    flood = [[0] * N for _ in range(N)]

    check(h)
    temp = 0
    for i in range(N):
        for j in range(N):
            if flood[i][j] == 0 and visited[i][j] == 0:
                bfs(i, j)
                temp += 1
    if safe < temp:
        safe = temp

print(safe)
