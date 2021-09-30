from collections import deque

# 나이트가 이동할 수 있는 8가지 방향
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def BFS():
    while queue:
        x, y = queue.popleft()

        # 목표지점에 도착하면 탈출
        if x == end_x and y == end_y:
            return graph[x][y] - 1

        # 8가지 방향 탐색
        for direction in range(8):
            nx = x + dx[direction]
            ny = y + dy[direction]

            # 범위 안에 있다면 증가, 큐에 계속 넣어주면서 진행
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))


T = int(input())

for tc in range(T):
    N = int(input())
    graph = [[0] * N for _ in range(N)]

    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    queue = deque()
    queue.append((start_x, start_y))
    graph[start_x][start_y] = 1

    move_cnt = BFS()

    print(move_cnt)
