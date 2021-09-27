# 미로 탐색
# 에디터
from collections import deque

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    global routes
    visited[r][c] = 1
    q = deque([[r, c, 1]])  # 길이를 들고다니면서 증가시키기
    while q:
        t = q.popleft()
        for d in range(4):
            nr = t[0] + dr[d]
            nc = t[1] + dc[d]
            if 0 <= nr < N and 0 <= nc < M and miro[nr][nc] == 1 and (visited[nr][nc] == 0):  # 범위, 값, 방문 체크
                visited[nr][nc] = 1
                if nr == N - 1 and nc == M - 1:  # (N,M)에 도달했으면 그때까지의 길이를 리스트에 추가
                    routes.append(t[2] + 1)
                else:
                    q.append([nr, nc, t[2] + 1])


# 입력
N, M = map(int, input().split())  # N:세로 M:가로
miro = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

routes = []  # 루트들을 담을 리스트
# (0,0)에서 출발
bfs(0, 0)
print(min(routes))
