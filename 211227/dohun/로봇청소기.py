N, M = map(int, input().split())

# 0은 북쪽, 1은 동쪽, 2는 남쪽, 3은 서쪽
x, y, direction = map(int, input().split())

# 맵 표시
graph = [list(map(int, input().split())) for _ in range(N)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 빈 칸은 0, 벽은 1
answer = 1 # 청소하는 칸의 개수

visited = [[0] * M for _ in range(N)]
visited[x][y] = 1
while True:
    check = False
    # 4방향 탐색
    for _ in range(4):
        # print("원방향", direction)
        direction = (direction - 1) % 4
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 방문하지 않았거나 벽이 아닐 경우에
        # if graph_check(nx, ny, visited):
        if graph[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            answer += 1
            x, y = nx, ny
            check = True
            break
    # 4벽이 이미 다 청소가 되어 있다면 후진
    if check == False:
        # print("방향" ,direction)
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 다시 청소 확인
        if graph[nx][ny] == 0:
            x, y = nx, ny
        # 전부 청소가 되어있으면 끝
        else:
            print(answer)
            break