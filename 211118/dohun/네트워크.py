n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def solution(n, computers):

    def DFS(i):
        visited[i] = 1
        # 연결되어 있는것 중에서 방문안한거면 들어가기
        for j in range(n):
            if computers[i][j] and not visited[j]:
                DFS(j)

    answer = 0 # 연결되어있는 개수
    visited = [0 for i in range(len(computers))]

    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1

    return answer

print(solution(n, computers))