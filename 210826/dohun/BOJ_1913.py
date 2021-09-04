N = int(input())
check_num = int(input())

# 시작할 숫자
number = N*N

graph = [[0] * N for _ in range(N)]

# 아래 오른쪽 위 왼쪽
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 방향과 0,0에서 시작
direction = 0
x, y = 0, 0

while True:
    # 숫자입력
    graph[x][y] = number
    # 방향에 따라서 숫자 입력
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 바깥에 벗어나면 방향을 바꿔준다.
    if nx < 0 or ny < 0 or nx >= N or ny >= N or graph[nx][ny] != 0:
        direction += 1
        # 방향이 4가 도달하면 다시 0으로 설정
        if direction == 4:
            direction = 0
        continue

    # 1에 도달하면 1을 채워주고 탈출
    x, y = nx, ny
    number -= 1
    if number == 1:
        graph[x][y] = 1
        break

# 2차원 배열을 출력해주고 M이라는 목표값을 찾아 위치를 출력해준다.
for i in range(N):
    for j in range(N):
        if graph[i][j] == check_num:
            check_x, check_y = i,j
        print(graph[i][j], end=' ')
    print()
print(check_x+1, check_y+1)