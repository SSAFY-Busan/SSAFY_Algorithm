# 섬의 개수
from collections import deque

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]


def bfs(r, c):
    q = deque([[r, c]])
    my_map[r][c] = 0
    while q:
        t = q.popleft()
        for d in range(8):
            nr = t[0] + dr[d]
            nc = t[1] + dc[d]
            if 0 <= nr < h and 0 <= nc < w and my_map[nr][nc] == 1:
                my_map[nr][nc] = 0
                q.append([nr, nc])


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        my_map = [list(map(int, input().split())) for _ in range(h)]
        ans = 0
        for r in range(h):
            for c in range(w):
                if my_map[r][c] == 1:
                    bfs(r, c)
                    ans += 1
        print(ans)
