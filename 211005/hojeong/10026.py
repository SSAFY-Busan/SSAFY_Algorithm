# 적록색약
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    q = deque([[r, c, painting[r][c]]])
    visited[r][c] = 1
    while q:
        t = q.popleft()
        for d in range(4):
            nr = t[0] + dr[d]
            nc = t[1] + dc[d]
            if 0 <= nr < N and 0 <= nc < N and (painting[nr][nc] == t[2]) and (visited[nr][nc] == 0):
                visited[nr][nc] = 1
                q.append([nr, nc, t[2]])


def person1():
    ans = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                bfs(r, c)
                ans += 1
    return ans


def person2():
    for r in range(N):
        for c in range(N):
            if painting[r][c] == 'G':
                painting[r][c] = 'R'
    return person1()


N = int(input())
painting = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
p1 = person1()
visited = [[0] * N for _ in range(N)]
p2 = person2()
print(p1, p2)
