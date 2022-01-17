# pypy로 해결..
from collections import deque

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y, visited, graph):
    global check
    people_number = graph[x][y] # 현재 인구
    count = 1 # 카운트
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    sub_lst = []
    sub_lst.append((x, y))

    while queue:
        x, y = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == 1:
                continue

            if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                people_number += graph[nx][ny]
                count += 1
                sub_lst.append((nx, ny))

    move_people = people_number // count

    if count > 1:
        check = True
        # 해당 점들 다 채워넣어주기
        for a, b in sub_lst:
            graph[a][b] = move_people


N, L, R = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

cnt = 0 # 인구이동 발생 카운트

while True:
    check = False # 인구이동 체크
    # 방문표시
    visited = [[0] * N for _ in range(N)]

    # 방문하지 않았으면 탐색해보기
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                BFS(i, j, visited, graph)

    # 체크면 인구이동 발생
    if check == True:
        cnt += 1
    else:
        break

print(cnt)