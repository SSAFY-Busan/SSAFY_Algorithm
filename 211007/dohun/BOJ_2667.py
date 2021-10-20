# 백준 2667번 단지번호 붙이기

from collections import deque

N = int(input())  # 지도의 크기
graph = [list(map(int, input())) for _ in range(N)]

# 이동할 4방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt_lst = []

# BFS 구현
def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    count = 1

    # 큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 공간을 벗어나는 경우 무시
            if nx >= 0 and ny >= 0 and nx < N and ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    cnt_lst.append(count)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            BFS(i, j)

cnt_lst.sort() # 영역이 작은것 부터 출력하기 위해서
print(len(cnt_lst)) # 영역 개수
for num in cnt_lst:
    print(num)