# 바이러스
from collections import deque


def bfs(start):
    virus[start] = 1  # 감염 체크
    q = deque()
    q.append(start)
    while q:
        top = q.popleft()
        for i in com[top]:
            if virus[i] == 0:
                bfs(i)  # return 생략가능?


def dfs(start):
    virus[start] = 1
    stack = []
    stack.append(start)
    while stack:
        top = stack.pop()
        for i in com[top]:
            if virus[i] == 0:
                dfs(i)


N = int(input())  # 컴퓨터 수
V = int(input())  # 간선 수

com = [[] for _ in range(N + 1)]
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
virus = [0] * (N + 1)
for i in range(V):
    s1, s2 = map(int, input().split())
    com[s1].append(s2)
    com[s2].append(s1)
# q=deque()
# bfs(1)
# stack=[]
dfs(1)
print(sum(virus) - 1)
