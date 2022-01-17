n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

def solution(n, results):
    answer = 0

    graph = [[0] * n for _ in range(n)]

    # 가위바위보 승자 표시
    for a,b in results:
        graph[a-1][b-1] = 1

    print(graph)
    # 순위를 아는 지점
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 경우가 있는 지점만 표시
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
    print(graph)

    for i in range(n):
        cnt = 0
        for j in range(n):
            if graph[i][j] or graph[j][i]:
                # print(i, j)
                cnt += 1
        # print(i, cnt)
        # 최대값 -1 한값이 순위를 매길 수 있는 선수들
        if cnt == n-1:
            answer += 1

    return answer


n = 5
results = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(solution(n, results))