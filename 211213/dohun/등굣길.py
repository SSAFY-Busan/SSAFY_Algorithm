M = 4
N = 3
puddles = [[2,2]]

def solution(M, N, puddles):
    graph = [[0] * (M) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                graph[i][j] = 1

            # 0일경우 인지 못했음.... 인덱스 에러가 안난다는걸
            # # puddles 인덱스 반대네....
            elif [j+1,i+1] not in puddles:
                graph[i][j] = graph[i-1][j] + graph[i][j-1]

                # 조건주기
                # if i == 0:
                #     graph[i][j] = graph[i][j - 1]
                # elif j == 0:
                #     graph[i][j] = graph[i - 1][j]
                # else:
                #     graph[i][j] = graph[i - 1][j] + graph[i][j - 1]

    # print(graph)
    # 마지막 나누기
    return graph[N-1][M-1] % 1000000007

print(solution(M, N, puddles))