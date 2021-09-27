# 그림
from collections import deque

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    size = 1
    q = deque([[r, c]])
    while q:
        t = q.popleft()
        for d in range(4):
            nr = t[0] + dr[d]
            nc = t[1] + dc[d]
            if 0 <= nr < n and 0 <= nc < m and paper[nr][nc] == 1 and (visited[nr][nc] == 0):  # 범위, 값, 방문 체크
                size += 1
                visited[nr][nc] = 1
                q.append([nr, nc])
    return size


# 입력
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]  # 방문체크
cnt = 0  # 개수 카운팅
results = []  # 크기 담을 리스트

# 전체 순회하면서 개수 체크
for r in range(n):
    for c in range(m):
        if paper[r][c] == 1 and visited[r][c] == 0:
            cnt += 1
            visited[r][c] = 1
            results.append(bfs(r, c))

# 출력
print(cnt)
# 개수가 0개일 경우 고려 -> 런타임 에러 해결
if cnt:
    print(max(results))
else:
    print(0)
