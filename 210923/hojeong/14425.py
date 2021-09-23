# 문자열 집합
N, M = map(int, input().split())  # N : 문자열 개수 M: 비교 문자열 개수
S = [input() for _ in range(N)]
ans = 0
for i in range(M):
    temp = input()
    if temp in S:
        ans += 1
print(ans)
