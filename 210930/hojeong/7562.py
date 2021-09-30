# 나이트의 이동
# 8방향
from collections import deque

dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs(r, c):
    visited[r][c] = 1
    q = deque([[r, c, 0]])
    while q:
        t = q.popleft()
        for d in range(8):
            nr = t[0] + dr[d]
            nc = t[1] + dc[d]
            if 0 <= nr < l and 0 <= nc < l and (visited[nr][nc] == 0):
                if nr == goal_r and nc == goal_c:
                    return t[2] + 1
                visited[nr][nc] = 1
                q.append([nr, nc, t[2] + 1])
    return 0


T = int(input())
for tc in range(T):
    l = int(input())
    cur_r, cur_c = map(int, input().split())
    goal_r, goal_c = map(int, input().split())
    visited = [[0] * l for _ in range(l)]  # 방문체크
    print(bfs(cur_r, cur_c))
