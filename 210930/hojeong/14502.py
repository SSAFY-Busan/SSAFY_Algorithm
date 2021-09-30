# 연구소
from collections import deque
from copy import deepcopy

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 안전 영역 찾기
def bfs():
    visited = deepcopy(origin_visited)
    space = deepcopy(origin_space)
    q = deque(virus)
    while q:
        t = q.popleft()
        visited[t[0]][t[1]] = 1
        for d in range(4):
            nr = t[0] + dr[d]
            nc = t[1] + dc[d]
            if 0 <= nr < N and 0 <= nc < M and space[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                space[nr][nc] = 2
                q.append((nr, nc))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if space[i][j] == 0:
                cnt += 1
    # print(space)
    # print(cnt)
    ans.append(cnt)


def set_wall(w):
    if w == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if origin_space[i][j] == 0:
                origin_space[i][j] = 1
                set_wall(w + 1)
                # print(w)
                origin_space[i][j] = 0


N, M = map(int, input().split())
origin_space = [list(map(int, input().split())) for _ in range(N)]
origin_visited = [[0] * M for _ in range(N)]
ans = []

# 발원지 찾기
virus = []
for r in range(N):
    for c in range(M):
        if origin_space[r][c] == 2:
            virus.append((r, c))

set_wall(0)
print(max(ans))
