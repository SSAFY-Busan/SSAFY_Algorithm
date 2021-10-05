from collections import deque

# 8방향 표시
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    # 큐 안에 들어있는 경우 계속 반복
    while queue:
        x, y = queue.popleft()

        # 8방향 확인 후 갈 수 있는 곳 가기
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            # 미로 범위안에 있으면
            if nx >= 0 and ny >= 0 and nx < H and ny < W and graph[nx][ny] == 1:
                # 방문한 곳을 다시 0으로 바꾸고 주변 탐색
                graph[nx][ny] = 0
                queue.append((nx, ny))


while True:
    # 넓이와 높이 입력받기
    W, H = map(int, input().split())

    # 높이와 넓이가 0이면 반복문 종료
    if W == 0 and H == 0:
        break

    # 섬 개수
    cnt = 0

    # 땅 표시
    graph = []
    for _ in range(H):
        graph.append(list(map(int, input().split())))

    # 방문한 곳이 땅이라면 주변을 수색
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1:
                BFS(i, j)
                cnt += 1

    print(cnt)