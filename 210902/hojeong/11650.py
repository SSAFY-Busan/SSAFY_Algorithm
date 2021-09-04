import sys

# 좌표 정렬하기
N = int(input())  # 점의 개수
n = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
n.sort(key=lambda x: (x[0], x[1]))  # 람다 이용해서 정렬
for i in range(N):
    print(*n[i])
