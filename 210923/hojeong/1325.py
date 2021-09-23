# 효율적인 해킹
import sys
from collections import deque

input = sys.stdin.readline


def bfs(n):
    visit = [0] * (N + 1)
    visit[n] = 1
    cnt = 1
    q = deque([n])
    while q:
        temp = q.popleft()
        for j in lst[temp]:
            if visit[j] == 0:
                visit[j] = 1
                cnt += 1
                q.append(j)
    return cnt


N, M = map(int, input().split())  # N: 컴퓨터의 수 M : 관계 수
lst = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    lst[b].append(a)  # a가 b를 신뢰한다.

sums = {}
for i in range(1, N + 1):
    sums[i] = bfs(i)
max_sum = max(sums.values())
for key, value in sums.items():
    if value == max_sum:
        print(key, end=' ')
