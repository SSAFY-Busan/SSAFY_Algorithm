from collections import deque

dx = [0, 1, 0, -1] # 우 하 좌 상
dy = [1, 0, -1, 0]

N = int(input()) # N은 보드 크기
graph = [[0] * N for _ in range(N)] # 필드

K = int(input()) # 사과의 개수
for _ in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 2 # 사과의 위치 표시

dir_lst = [0 for _ in range(10001)] # 공간 표시
L = int(input()) # 방향 변환 횟수
for _ in range(L):
    game_time, direct = input().split() # 시간과 방향
    dir_lst[int(game_time)] = direct

queue = deque()
queue.append((0,0)) # 뱀 시작
graph[0][0] = 1
direction = 0 # 방향
time_check = 1 # 시간 체크
nx, ny = 0, 1

# 범위 안에 있을 경우고 갈 수 있는 곳이면
while 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != 1:
    queue.append((nx, ny))
    if graph[nx][ny] == 2: # 사과를 발견하면 변경
        graph[nx][ny] = 1

    elif graph[nx][ny] == 1: # 방문한것은 그냥 탈출
        break

    else: # 0일경우
        graph[nx][ny] = 1
        x, y = queue.popleft() # 스택에 남아있는거 다시 전환
        graph[x][y] = 0

    # X초가 지나면 방향전환
    if dir_lst[time_check] == 'L':
        direction = (direction - 1) % 4
    elif dir_lst[time_check] == 'D':
        direction = (direction + 1) % 4

    time_check += 1 # 시간 증가
    # 옮겨가긱
    nx += dx[direction]
    ny += dy[direction]

print(time_check)
