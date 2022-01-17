def dragon_curve(x, y, direction, gen, graph):
    graph[x][y] = 1
    x, y = x+dx[direction], y+dy[direction]
    # 처음 방향대로 가기
    graph[x][y] = 1

    stack = [direction]

    for i in range(gen):
        len_stack = len(stack)

        # print("세대 들어가기")
        for g in range(len_stack-1, -1, -1):
            # 역순의 + 1
            n = (stack[g] + 1) % 4
            x, y = x+dx[n], y+dy[n]
            graph[x][y] = 1

            stack.append(n)
            # print("스택", stack)

# 드래곤커브개수
N = int(input())

# 주어진 순서대로 방향
# 0 오른쪽, 1 위, 2 왼쪽, 3 아래
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

graph = [[0 for _ in range(101)] for _ in range(101)]

for i in range(N):
    # x, y, 방향, 세대
    x, y, direction, gen = map(int, input().split())

    # 여긴 반대로 넣어줘야함
    dragon_curve(y, x, direction, gen, graph)

cnt = 0

for i in range(101):
    for j in range(101):
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
            cnt += 1

print(cnt)
# print(graph)