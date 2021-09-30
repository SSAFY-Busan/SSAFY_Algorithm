# 토마토
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    while q:
        t = q.popleft()
        for d in range(4):
            nr = t[0] + dr[d]
            nc = t[1] + dc[d]
            if 0 <= nr < N and 0 <= nc < M and (visited[nr][nc] == -1):
                visited[nr][nc] = t[2] + 1  # 날짜 저장
                q.append([nr, nc, t[2] + 1])


def check():
    day = 0  # 날짜
    for i in range(N):
        if -1 in visited[i]:  # 방문하지 못했다면==안익은 토마토가 있다면
            return -1
        else:
            temp = max(visited[i])  # 방문배열에 가장 큰 값이 걸리는 날짜
            if temp > day:
                day = temp
    return day


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]  # 방문 & 날짜 저장

q = deque([])
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 1:
            q.append([r, c, 0])
            visited[r][c] = 0
        elif tomato[r][c] == -1:
            visited[r][c] = 0
bfs()
print(check())
