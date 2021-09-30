from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x,y = queue.popleft()

        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                queue.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
queue = deque([])
sub_check = False # 익은 토마토 찾기

# 익은 토마토만 찾기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i,j])

# 익은 토마토가 없으면 체크
if len(queue) == 0:
    sub_check = True

bfs()

check = False # 익은것이 없는 것 확인
answer = 0

# 0이 있다면 익지 못한것이므로 체크 표시
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            check = True
            break
        # 0 이 아니라면 계속 최대값 갱신
        answer = max(answer, graph[i][j])

# 1이 한개도 없으면 익을 수 없기 때문에 sub_check True 만들어주기
if check == True: # 익지 않은것이 하나라도 있다면
    print(-1)
elif sub_check == True: # 익은 토마토가 없으면
    print(0)
# 걸리는 날짜 표시
else:
    print(answer-1)