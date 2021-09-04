N = int(input())
graph = [[0] * 101 for _ in range(101)]
answer = 0
for _ in range(N):
    a, b = map(int, input().split())
    # 길이는 10칸이라서 +10
    for i in range(a, a+10):
        for j in range(b, b+10):
            graph[j][i] = 1

# 영역 1개당 카운트 1
for i in range(101):
    for j in range(101):
        if graph[i][j] == 1:
            answer += 1

print(answer)