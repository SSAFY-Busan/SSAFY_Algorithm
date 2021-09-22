# python은 왜 안되는걸까..? pypy3도 엄청오래걸림..

from collections import deque
import sys

def BFS(start):
    cnt = 1 # 처음 갯수
    queue = deque([start])
    visited = [0 for _ in range(N+1)]
    visited[start] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1
    return cnt

# N은 컴퓨터 대수, M은 신뢰관계
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    # b를 해킹하면 a가 해킹이 된다.
    a, b = map(int, input().split())
    graph[b].append(a)

cnt_lst = []
max_cnt = 0 # 최대
for num in range(1, N+1):
    cnt = BFS(num)
    if max_cnt == cnt:
        cnt_lst.append(num)

    if max_cnt < cnt:
        max_cnt = cnt
        cnt_lst = []
        cnt_lst.append(num)

print(*cnt_lst)