N, M, x, y, K = map(int, input().split())

graph = []
# 북쪽부터 남쪽으로, 서쪽부터 동쪽
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 동쪽:1, 서쪽:2, 북쪽:3, 남쪽:4
# 마지막 이동하는 명령
arr = list(map(int, input().split()))

dice = [0] * 6
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for direction in arr:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 <= nx < N and 0 <= ny < M:
        if direction == 1:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
        elif direction == 2:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
        elif direction == 3:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
        elif direction == 4:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]

         # 0일 경우 바닥면 출력
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[5]
        else:
            graph[nx][ny], dice[5] = 0, graph[nx][ny]
        # 윗면 출력
        print(dice[0])
        x, y = nx, ny