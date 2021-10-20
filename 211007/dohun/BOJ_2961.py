N = int(input())

foods = [list(map(int, input().split())) for _ in range(N)]

min_diff = 1000000000
for i in range(1, 1 << N):
    S, B = 1, 0 # 신맛은 곱셈, 쓴맛은 합
    for j in range(N):
        if i & 1 << j:
            print(i & 1 << j)
            S *= foods[j][0]
            B += foods[j][1]

    min_diff = min(min_diff, abs(S - B))

print(min_diff)
