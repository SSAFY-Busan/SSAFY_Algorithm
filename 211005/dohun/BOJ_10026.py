from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(i,j,color):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if color == 'B':
                if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 'B' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

            elif color == 'G':
                if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 'G' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

            elif color == 'R':
                if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 'R' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


def BFS2(i,j,color):
    queue = deque()
    queue.append((i,j))
    visited2[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if color == 'B':
                if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 'B' and visited2[nx][ny] == 0:
                    visited2[nx][ny] = 1
                    queue.append((nx, ny))

            elif color == 'G' or color == 'R':
                if 0 <= nx < N and 0 <= ny < N and (graph[nx][ny] == 'G' or graph[nx][ny] =='R') and visited2[nx][ny] == 0:
                    visited2[nx][ny] = 1
                    queue.append((nx, ny))


N = int(input())

graph = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

RGB = 0
# 3개다 구별가능
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R' and visited[i][j] == 0:
            BFS(i,j,'R')
            RGB += 1
        elif graph[i][j] == 'G' and visited[i][j] == 0:
            BFS(i,j,'G')
            RGB += 1
        elif graph[i][j] == 'B' and visited[i][j] == 0:
            BFS(i,j,'B')
            RGB += 1

# 2개만 구별 가능
RGB_2 = 0
visited2 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R' and visited2[i][j] == 0:
            BFS2(i,j,'R')
            RGB_2 += 1
        elif graph[i][j] == 'G' and visited2[i][j] == 0:
            BFS2(i,j,'G')
            RGB_2 += 1
        elif graph[i][j] == 'B' and visited2[i][j] == 0:
            BFS2(i,j,'B')
            RGB_2 += 1

print("{} {}".format(RGB, RGB_2))