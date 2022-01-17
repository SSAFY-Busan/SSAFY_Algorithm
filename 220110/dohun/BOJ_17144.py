from collections import deque

R, C, T = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def air_spread():
    global graph

    visited = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                cnt = 0
                move_dust = graph[i][j] // 5

                for direction in range(4):
                    nx = i + dx[direction]
                    ny = j + dy[direction]

                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        visited[nx][ny] += move_dust
                        cnt += 1

                visited[i][j] -= (move_dust * cnt)

    for i in range(R):
        for j in range(C):
            graph[i][j] += visited[i][j]

def clean(m, dxdy):
    direction = 0
    nx = m
    ny = 0
    temp = 0
    while direction < 4:
        nx += dxdy[direction][0]
        ny += dxdy[direction][1]

        if nx == m and ny == 0:
            return

        if 0 <= nx < R and 0 <= ny < C:
            temp, graph[nx][ny] = graph[nx][ny], temp
        else:
            nx -= dxdy[direction][0]
            ny -= dxdy[direction][1]
            direction+= 1

air_machine = 0
for i in range(R):
    if graph[i][0] == -1:
        air_machine = i
        break

for _ in range(T):
    air_spread()

    dxdy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    clean(air_machine, dxdy)

    dxdy2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    clean(air_machine+1, dxdy2)

print(sum(map(sum, graph)) + 2)
