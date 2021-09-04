def DFS(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            DFS(i)
    return cnt

import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스
for tc in range(T):
    N, M = map(int, input().split()) # N은 국가수, M은 비행기 수
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    cnt = 0

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # print(N-1)
    result = DFS(1)
    print(result)