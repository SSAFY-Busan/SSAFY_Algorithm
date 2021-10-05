dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def BFS():
    while queue:
        z, x, y = queue.popleft()

        for direction in range(6):
            nx = x + dx[direction]
            ny = y + dy[direction]
            nz = z + dz[direction]

            if 0 <= nz < H and 0 <= ny < M and 0 <= nx < N:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    queue.append((nz, nx, ny))

from collections import deque

# M은 가로, N은 세로, H는 상자 수
M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

BFS()

fruit_check = False # 0이 있는지 확인 -> 익지 못한 것
day_cnt = 0 # 일수 계산 변수

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                fruit_check = True # 익지못한것을 발견하면 True

            # 익는데 걸리는 최대 날짜 갱신
            day_cnt = max(day_cnt, graph[i][j][k])

# 익지 못한것이 있을 경우
if fruit_check == True:
    print(-1)
# 최대값이 1이면 전부 익어있는 상태
elif day_cnt == 1:
    print(0)
else:
    print(day_cnt-1)