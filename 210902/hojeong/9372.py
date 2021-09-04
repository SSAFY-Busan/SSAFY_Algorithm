# 상근이의 여행
import sys


def bfs(a):
    q = [a]
    visited[a] = 1
    cnt = 0
    while q:
        temp = q.pop(0)
        for i in node[temp]:
            if visited[i] == 0:
                visited[i] = 1  # 방문체크
                cnt += 1
                q.append(i)
    return cnt


T = int(sys.stdin.readline())  # 테스트케이스 수
for tc in range(T):
    N, M = map(int, sys.stdin.readline().split())  # N:나라수 M:비행기 종류
    node = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)  # 방문체크
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        node[a].append(b)  # 왕복이니깐
        node[b].append(a)
    ans = 0
    for i in range(N):
        if visited[i] == 0:
            ans += bfs(i)
    print(ans)
# print(N-1)
