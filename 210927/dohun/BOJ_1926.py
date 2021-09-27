from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x,y, cnt_lst):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나는 경우 패스
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 그림이 없는 경우 패스
            if graph[nx][ny] == 0:
                continue

            # 그림이 존재하고 방문하지 않은 경우
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1

    cnt_lst.append(cnt)

N, M = map(int, input().split()) # N은 세로 M은 가로

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt_lst = []
image_count = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and visited[i][j] == 0:
            BFS(i,j, cnt_lst)
            image_count += 1

# 그림이 없을 경우 0을 출력
if len(cnt_lst) == 0:
    print(0)
    print(0)
else:
    print(image_count)
    print(max(cnt_lst))