# 숨바꼭질
from collections import deque


def bfs(n):
    q = deque([n])
    distance[n] = 1  # 시작 거리를 1로
    while q:
        t = q.popleft()
        for k in g[t]:
            if distance[k] == 0:
                distance[k] = distance[t] + 1
                q.append(k)


N, M = map(int, input().split())  # N: 헛간의 개수 M: 양방향 길
g = [[] for _ in range(N + 1)]  # 0번 인덱스부터
distance = [0] * (N + 1)  # 거리체크
for i in range(M):
    s, e = map(int, input().split())
    g[s].append(e)  # 양방향
    g[e].append(s)
bfs(1)  # 1번부터 찾는다
ans = max(distance)  # 최대거리
print(distance.index(ans), ans - 1, distance.count(ans))
