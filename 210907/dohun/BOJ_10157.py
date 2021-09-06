col, row = map(int, input().split()) # col은 가로 row는 세로

graph = [[0] * (col) for _ in range(row)]
N = int(input())

check_num = False

# 방향 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 찾을 숫자가 가로와 세로곱한것 보다 크면 체크하기
if N > row * col:
    check_num = True


cnt = 1 # 입력할 숫자
x, y = row -1, 0 # 시작 위치
direction = 0 # 방향

# 체크가 되었으면 0을 출력 아닐경우 그래프 채우면서 시작
if check_num == True:
    print(0)
else:
    while True:
        # 그래프에 입력하고 다음 숫자 입력
        graph[x][y] = cnt
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위밖에 있거나 이미 입력되어 있다면 방햐을 바꾼다.
        if nx < 0 or ny < 0 or nx >= row or ny >= col or graph[nx][ny] != 0:
            direction += 1
            if direction == 4:
                direction = 0
            nx = x + dx[direction]
            ny = y + dy[direction]

        x, y = nx, ny
        cnt += 1

        # 끝까지 다 입력하면 끝
        if cnt == row*col+1:
            break

    # 숫자의 위치를 탐색한다.
    for i in range(row):
        for j in range(col):
            if graph[i][j] == N:
                x, y = i, j
                break

    print(y+1, row-x)