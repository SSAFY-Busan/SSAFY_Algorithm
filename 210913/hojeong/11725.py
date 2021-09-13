# 트리의 부모 찾기
import sys

sys.setrecursionlimit(10 ** 9)


def dfs(st):
    for i in tree[st]:
        if parents[i] == 0:  # 부모가 없으면
            parents[i] = st
            print(parents)
            dfs(i)


N = int(sys.stdin.readline())

tree = [[] for i in range(N + 1)]  # 0번부터 생성
parents = [0 for i in range(N + 1)]  # 부모 리스트

for i in range(N - 1):
    s1, s2 = map(int, sys.stdin.readline().split())
    tree[s1].append(s2)
    tree[s2].append(s1)
# [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

dfs(1)
for i in range(2, N + 1):  # 2번 노드의 부모부터 출력
    print(parents[i])
