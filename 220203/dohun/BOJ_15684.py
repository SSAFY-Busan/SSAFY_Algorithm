def check():
    for i in range(N):
        # 이동하는 세로선 위치
        now = i
        # print("시작")
        # print(graph)
        for j in range(H):
            # print(now)
            # 오른쪽이 1인경우
            if graph[j][now] == 1:
                now += 1
            # 왼쪽이 1인경우
            elif now > 0 and graph[j][now -1]:
                now -= 1

        # print(i, now)
        if now != i:
            return False
    return True


def DFS(cnt, start, limit_cnt):
    global answer
    # 가능한 길을 다쓸 때
    if cnt == limit_cnt:
        if check() == False:
            return False
        else:
            if answer > limit_cnt:
                answer = limit_cnt
            return True

    # 행 돌기기
    for i in range(start, H):
        # 열 돌기
        for j in range(N-1):
            # 사다리가 있을 때
            if graph[i][j] == 1:
                continue
            # 사다리가 없을 때
            if graph[i][j] == 0:
                # 범위를 나가지 않고 왼쪽에 사다리가 있는 경우
                if j - 1 > -1 and graph[i][j-1] == 1:
                    continue
                # 범위를 나가지 않고 오른쪽에 사다리가 있는 경우
                if j + 1 <= N - 2 and graph[i][j+1] == 1:
                    continue
            # 해당 조건이 없으면 사다리 놓기
            graph[i][j] = 1

            # 마지막 행부터 다시 시작하기기
            if DFS(cnt+1, i, limit_cnt):
                return True
            # 되돌리기
            graph[i][j] = 0

# N은 세로선, M은 가로선
# H는 세로선마다 가로선을 놓을 수 있는 위치의 개수
N, M, H = map(int, input().split())

graph = [[0] * N for _ in range(H)]
answer = 987654321

for _ in range(M):
    # 가로세로선
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for i in range(4):
    num = DFS(0, 0, i)
    if num == True:
        break

if answer == 987654321:
    print(-1)
else:
    print(answer)