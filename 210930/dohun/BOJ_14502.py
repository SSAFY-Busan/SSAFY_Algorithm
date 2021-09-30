# 연구소
N, M = map(int, input().split())

# 초기맵
block_map = [[0] * M for _ in range(N)]
graph = [list(map(int, input().split())) for _ in range(N)]

# 4가지 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0 # 안전영역

# DFS를 이용해서 바이러스 퍼지기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상하좌우 퍼지는 경우
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if block_map[nx][ny] == 0:
                # 바이러스 퍼지는것 적용
                block_map[nx][ny] = 2
                virus(nx, ny)

def score():
    score = 0
    for i in range(N):
        for j in range(M):
            # 빈공간일때마다 1점으로 생각해서 점수 리턴
            if block_map[i][j] == 0:
                score += 1
    return score


# DFS 이용하여 안전 영역 크기 계산하기
def DFS(count):
    global result
    # 울타리가 3개 설치되었을 경우
    if count == 3:
        for i in range(N):
            for j in range(M):
                block_map[i][j] = graph[i][j]

        # 각 바이러스 위치에서 전파 진행
        for i in range(N):
            for j in range(M):
                # 바이러스 발견하면
                if block_map[i][j] == 2:
                    virus(i, j)

        # 안전 영역 최대값 계산
        result = max(result, score())
        return

    # 빈 공간에 울타리 설치
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                DFS(count)
                graph[i][j] = 0
                count -= 1


DFS(0)
print(result)