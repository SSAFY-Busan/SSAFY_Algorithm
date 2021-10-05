# 토마토
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
dz = [-1, 1]


def bfs():
    while q:
        t = q.popleft()
        for d in range(4):
            nr = t[1] + dr[d]
            nc = t[2] + dc[d]
            if 0 <= nr < N and 0 <= nc < M and box[t[0]][nr][nc] == 0:
                box[t[0]][nr][nc] = t[3] + 1
                q.append([t[0], nr, nc, t[3] + 1])
        for z in range(2):
            nz = t[0] + dz[z]
            if 0 <= nz < H and box[nz][t[1]][t[2]] == 0:
                box[nz][t[1]][t[2]] = t[3] + 1
                q.append([nz, t[1], t[2], t[3] + 1])


def zero_count():
    cnt = 0
    for h in range(H):
        for r in range(N):
            cnt += box[h][r].count(0)
    return cnt


M, N, H = map(int, input().split())
box = [[[0] * M for _ in range(N)] for _ in range(H)]
for h in range(H):
    for r in range(N):
        box[h][r] = list(map(int, input().split()))

# 저장될 떄부터 모두 토마토가 익어있는 상태
zero_cnt = zero_count()
if zero_cnt == 0:
    print(0)
else:
    q = deque([])
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if box[h][r][c] != 0:
                    if box[h][r][c] == 1:
                        q.append([h, r, c, 0])
    bfs()
    # 모두 익었는지
    zero_cnt = zero_count()
    if zero_cnt > 0:
        print(-1)
    else:
        ans = 0
        for h in range(H):
            for r in range(N):
                temp = max(box[h][r])
                if ans < temp:
                    ans = temp
        print(ans)
