triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    # 같은 크기의 배열 만들기
    graph = [[0] * len(triangle) for _ in range(len(triangle))]
    graph[0][0] = triangle[0][0] # 초기점 찍기

    # 세로
    for i in range(len(triangle) - 1):
        # 가로
        for j in range(len(triangle[i])):
            # 자신의 한칸밑에 왼쪽
            graph[i+1][j] = max(graph[i+1][j], graph[i][j] + triangle[i+1][j])
            # 자신의 한칸밑에 오른쪽
            graph[i+1][j+1] = max(graph[i+1][j+1], graph[i][j] + triangle[i+1][j+1])
            # graph[i+1][j+1] = graph[i][j] + triangle[i+1][j+1]
# i==0이랑 i==j일때 처리해주기 => 더 줄어듬
# triangle자체에 갱신하면 더 줄어듬
    return max(graph[-1])


print(solution(triangle))