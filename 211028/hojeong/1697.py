# 숨바꼭질
from collections import deque


def bfs():
    q = deque([[N, 0]])
    visited[N] = 1
    while q:
        t = q.popleft()
        if t[0] == K:
            return t[1]
        for i in range(3):
            if i == 0:
                nt = t[0] + 1
            elif i == 1:
                nt = t[0] - 1
            elif i == 2:
                nt = t[0] * 2
            if 0 <= nt <= 100000 and not visited[nt]:
                visited[nt] = 1
                q.append([nt, t[1] + 1])


N, K = map(int, input().split())
visited = [0] * 100001
ans = bfs()
print(ans)
