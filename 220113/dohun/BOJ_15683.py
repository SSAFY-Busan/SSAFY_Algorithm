from collections import deque

N, M = map(int, input().split())

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

graph = [list(map(int, input().split())) for _ in range(N)]
cctv_lst = []
answer = 0 # 사각지대
visited = [[0] * M for _ in range(N)]
cctv_cnt = 0 # cctv 개수

def solution(count):
    global visited, answer
    # CCTV 개수 전부 체크했다면 사각지대 확인하기
    if count == cctv_cnt:
        sub_cnt = 0
        for i in range(N):
            for j in range(M):
                # 사각지대 체크하기
                if graph[i][j] == 0 and visited[i][j] == 0:
                    sub_cnt += 1
        return sub_cnt

    # CCTV 확인하기
    x, y = cctv_lst[count][0], cctv_lst[count][1]
    for direction in range(4):
        arr = []
        if graph[x][y] == 1:
            arr.append(direction)
        elif graph[x][y] == 2:
            arr.append(direction)
            arr.append((direction + 2) % 4)
        elif graph[x][y] == 3:
            arr.append(direction)
            arr.append((direction - 1) % 4)
        elif graph[x][y] == 4:
            arr.append(direction)
            arr.append((direction - 1) % 4)
            arr.append((direction + 2) % 4)
        elif graph[x][y] == 5:
            arr.append(direction)
            arr.append((direction - 1) % 4)
            arr.append((direction + 1) % 4)
            arr.append((direction + 2) % 4)
        queue = deque()
        # CCTV 방향 확인
        for a in arr:
            nx, ny = x + dx[a], y + dy[a]
            # 범위 안에 들면 계속 그 방향으로 가기
            while 0 <= nx < N and 0 <= ny < M:
                # 방문하지 않았고 벽이 아니라면
                if visited[nx][ny] == 0 and graph[nx][ny] != 6:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                # 벽이면 끝
                elif graph[nx][ny] == 6:
                    break
                nx += dx[a]
                ny += dy[a]
        # 작은거 비교하며 다음 cctv 호출하기
        answer = min(answer, solution(count + 1))

        # 되돌아가기
        while queue:
            qx, qy = queue.popleft()
            if graph[qx][qy] == 0:
                visited[qx][qy] = 0

        # 5번은 전체
        if graph[x][y] == 5:
            break

    return answer


for i in range(N):
    for j in range(M):
        # CCTV 체크
        if 0 < graph[i][j] < 6:
            cctv_lst.append((i, j))
            visited[i][j] = 1
            cctv_cnt += 1
        # 사각지대 체크
        if graph[i][j] == 0:
            answer += 1

solution(0)
print(answer)
